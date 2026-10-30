"""
main.py - አማላጅ ፕላስ (Amalaj Plus) FastAPI backend.

Run:  uvicorn main:app --reload
Env:  SECRET_KEY (required in prod), BOT_API_KEY, DATABASE_URL, CORS_ORIGINS, ADMIN_PHONE/ADMIN_PASSWORD (first admin)
"""
import asyncio
import hashlib
import hmac
import os
import re
import secrets
import uuid
from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Literal

import jwt  # PyJWT
from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from models import (
    OPEN_ESCROW_STATUSES, DealMessage, EscrowStatus, EscrowTransaction, Listing,
    ListingStatus, PlatformType, SessionLocal, User, VerificationLog,
    calc_commission, init_db, utcnow,
)

SECRET_KEY = os.getenv("SECRET_KEY", "")
if not SECRET_KEY:
    SECRET_KEY = secrets.token_hex(32)
    print("WARNING: SECRET_KEY not set - using a random key; sessions reset on restart.")
BOT_API_KEY = os.getenv("BOT_API_KEY", "")
TOKEN_TTL_HOURS = 24
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads"))
UPLOAD_DIR.mkdir(exist_ok=True)
MAX_UPLOAD_BYTES = 5 * 1024 * 1024
IMAGE_SIGNATURES = {b"\xff\xd8\xff": ".jpg", b"\x89PNG\r\n\x1a\n": ".png", b"RIFF": ".webp"}

# Recovery scams are most common on accounts tied to phone/email recovery, so those get 7 days by default.
DEFAULT_COOLDOWN_DAYS = {
    "TikTok": 7, "YouTube": 7, "Instagram": 7, "Facebook": 7, "X_Twitter": 7,
    "Telegram": 5, "Website_SaaS": 3,
}


# ----------------------------------------------------------------------------- app / lifecycle
def release_due_escrows() -> int:
    """Release funds for deals whose cooldown has elapsed with no dispute. Safe to call repeatedly."""
    released = 0
    with SessionLocal() as db:
        due = db.scalars(
            select(EscrowTransaction)
            .where(EscrowTransaction.status == EscrowStatus.Buyer_Verification_Period,
                   EscrowTransaction.cooldown_ends_at <= utcnow())
            .with_for_update()
        ).all()
        for tx in due:
            complete_deal(db, tx)
            released += 1
        db.commit()
    return released


async def cooldown_worker():
    while True:
        try:
            await asyncio.to_thread(release_due_escrows)
        except Exception as exc:  # never let the worker die
            print("cooldown_worker error:", exc)
        await asyncio.sleep(60)


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    seed_admin()
    task = asyncio.create_task(cooldown_worker())
    yield
    task.cancel()


app = FastAPI(title="Amalaj Plus API", version="1.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000").split(","),
    allow_methods=["*"], allow_headers=["*"],
)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


def get_db():
    with SessionLocal() as db:
        yield db


def seed_admin():
    phone, pw = os.getenv("ADMIN_PHONE"), os.getenv("ADMIN_PASSWORD")
    if not (phone and pw):
        return
    phone = normalize_phone(phone)
    with SessionLocal() as db:
        if not db.scalar(select(User).where(User.phone_number == phone)):
            db.add(User(full_name="Admin", phone_number=phone, password_hash=hash_password(pw),
                        is_admin=True, is_verified=True))
            db.commit()


# ----------------------------------------------------------------------------- auth helpers
def hash_password(pw: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.scrypt(pw.encode(), salt=salt, n=2**14, r=8, p=1)
    return f"scrypt${salt.hex()}${digest.hex()}"


def verify_password(pw: str, stored: str) -> bool:
    try:
        _, salt, digest = stored.split("$")
        calc = hashlib.scrypt(pw.encode(), salt=bytes.fromhex(salt), n=2**14, r=8, p=1)
        return hmac.compare_digest(calc.hex(), digest)
    except ValueError:
        return False


def make_token(user: User) -> str:
    exp = datetime.now(timezone.utc) + timedelta(hours=TOKEN_TTL_HOURS)
    return jwt.encode({"sub": str(user.id), "exp": exp}, SECRET_KEY, algorithm="HS256")


bearer = HTTPBearer(auto_error=False)


def current_user(cred: HTTPAuthorizationCredentials | None = Depends(bearer), db: Session = Depends(get_db)) -> User:
    if not cred:
        raise HTTPException(401, "Not authenticated")
    try:
        uid = int(jwt.decode(cred.credentials, SECRET_KEY, algorithms=["HS256"])["sub"])
    except (jwt.PyJWTError, ValueError, KeyError):
        raise HTTPException(401, "Invalid or expired token")
    user = db.get(User, uid)
    if not user:
        raise HTTPException(401, "User not found")
    return user


def admin_user(user: User = Depends(current_user)) -> User:
    if not user.is_admin:
        raise HTTPException(403, "Admin only")
    return user


def bot_auth(x_bot_key: str = Header(default="")):
    if not BOT_API_KEY or not hmac.compare_digest(x_bot_key, BOT_API_KEY):
        raise HTTPException(401, "Invalid bot key")


# ----------------------------------------------------------------------------- schemas
PHONE_RE = r"^(\+251|0)?[79]\d{8}$"


class RegisterIn(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    phone_number: str = Field(pattern=PHONE_RE)
    password: str = Field(min_length=8, max_length=128)
    email: str | None = Field(default=None, pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    telegram_id: int | None = None


class LoginIn(BaseModel):
    identifier: str  # phone or email
    password: str


class EscrowIn(BaseModel):
    listing_id: int
    agreed_amount_etb: Decimal = Field(gt=0, max_digits=14, decimal_places=2)
    cooldown_days: int | None = Field(default=None, ge=3, le=7)


class DisputeIn(BaseModel):
    reason: str = Field(min_length=10, max_length=2000)


class MessageIn(BaseModel):
    body: str = Field(min_length=1, max_length=2000)


class ResolveIn(BaseModel):
    outcome: Literal["release_to_seller", "refund_buyer"]
    note: str = Field(min_length=3, max_length=2000)


class BotListingIn(BaseModel):
    telegram_id: int
    handle: str
    account_title: str
    category: str
    followers_subscribers_count: int = Field(ge=0)
    monthly_revenue_etb: Decimal = Field(default=0, ge=0)
    asking_price_etb: Decimal = Field(gt=0)
    description: str = ""
    engagement_rate: float | None = None
    fake_followers_score: float | None = None  # None = could not measure -> manual review
    bot_verified: bool = False


# ----------------------------------------------------------------------------- serializers
def valuation_tag(l: Listing) -> str:
    """Rough price signal: revenue multiple when revenue exists, otherwise ETB per follower."""
    price, rev = float(l.asking_price_etb), float(l.monthly_revenue_etb or 0)
    if rev > 0:
        months = price / rev
        return "Very Good Price" if months <= 18 else "Fair Price" if months <= 36 else "High Price"
    per_k = price / max(l.followers_subscribers_count, 1) * 1000
    return "Very Good Price" if per_k <= 1500 else "Fair Price" if per_k <= 5000 else "High Price"


def listing_out(l: Listing, detail: bool = False) -> dict:
    d = {
        "id": l.id, "platform_type": l.platform_type.value, "account_title": l.account_title,
        "category": l.category, "followers_subscribers_count": l.followers_subscribers_count,
        "monthly_revenue_etb": float(l.monthly_revenue_etb), "asking_price_etb": float(l.asking_price_etb),
        "status": l.status.value, "engagement_rate": l.engagement_rate, "quality_score": l.quality_score,
        "valuation_tag": valuation_tag(l), "created_at": l.created_at.isoformat(),
        "seller_id": l.seller_id,
    }
    if detail:
        d["description"] = l.description
        d["proof_image_url"] = l.proof_image_url
        d["seller_verified"] = l.seller.is_verified
    return d


def escrow_out(tx: EscrowTransaction) -> dict:
    return {
        "id": tx.id, "listing_id": tx.listing_id, "listing_title": tx.listing.account_title,
        "buyer_id": tx.buyer_id, "seller_id": tx.seller_id,
        "agreed_amount_etb": float(tx.agreed_amount_etb), "commission_fee_etb": float(tx.commission_fee_etb),
        "seller_payout_etb": float(tx.agreed_amount_etb - tx.commission_fee_etb),
        "status": tx.status.value, "cooldown_days": tx.cooldown_days,
        "cooldown_ends_at": tx.cooldown_ends_at.isoformat() if tx.cooldown_ends_at else None,
        "payment_reference": tx.payment_reference, "dispute_reason": tx.dispute_reason,
        "resolution_note": tx.resolution_note,
        "created_at": tx.created_at.isoformat(), "updated_at": tx.updated_at.isoformat(),
    }


# ----------------------------------------------------------------------------- auth routes
@app.post("/auth/register", status_code=201)
def register(body: RegisterIn, db: Session = Depends(get_db)):
    phone = normalize_phone(body.phone_number)
    clash = db.scalar(select(User).where(or_(User.phone_number == phone,
                                             User.email == body.email if body.email else False,
                                             User.telegram_id == body.telegram_id if body.telegram_id else False)))
    if clash:
        raise HTTPException(409, "Phone, email or Telegram ID already registered")
    user = User(full_name=body.full_name.strip(), phone_number=phone, email=body.email,
                telegram_id=body.telegram_id, password_hash=hash_password(body.password))
    db.add(user)
    db.commit()
    return {"token": make_token(user), "user": me_out(user)}


@app.post("/auth/login")
def login(body: LoginIn, db: Session = Depends(get_db)):
    ident = body.identifier.strip()
    user = db.scalar(select(User).where(or_(User.email == ident, User.phone_number == normalize_phone(ident))))
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(401, "Wrong phone/email or password")
    return {"token": make_token(user), "user": me_out(user)}


@app.get("/me")
def me(user: User = Depends(current_user)):
    return me_out(user)


def me_out(u: User) -> dict:
    return {"id": u.id, "full_name": u.full_name, "is_admin": u.is_admin, "is_verified": u.is_verified}


def normalize_phone(p: str) -> str:
    p = re.sub(r"[\s-]", "", p)
    return "+251" + p[-9:] if re.fullmatch(PHONE_RE, p) else p


# ----------------------------------------------------------------------------- listings
def save_proof_image(file: UploadFile) -> str:
    data = file.file.read(MAX_UPLOAD_BYTES + 1)
    if len(data) > MAX_UPLOAD_BYTES:
        raise HTTPException(413, "Image must be 5 MB or smaller")
    ext = next((e for sig, e in IMAGE_SIGNATURES.items() if data.startswith(sig)), None)
    if not ext:  # trust file contents, not the client-supplied content-type
        raise HTTPException(415, "Proof must be a JPG, PNG or WebP image")
    name = f"{uuid.uuid4().hex}{ext}"
    (UPLOAD_DIR / name).write_bytes(data)
    return f"/uploads/{name}"


@app.post("/listings", status_code=201)
def create_listing(
    platform_type: PlatformType = Form(...),
    account_title: str = Form(..., min_length=3, max_length=160),
    category: str = Form(..., max_length=80),
    followers_subscribers_count: int = Form(..., ge=0),
    monthly_revenue_etb: Decimal = Form(0, ge=0),
    asking_price_etb: Decimal = Form(..., gt=0),
    description: str = Form("", max_length=5000),
    handle: str | None = Form(None, max_length=160),
    proof_image: UploadFile = File(...),
    user: User = Depends(current_user),
    db: Session = Depends(get_db),
):
    listing = Listing(
        seller_id=user.id, platform_type=platform_type, account_title=account_title, category=category,
        followers_subscribers_count=followers_subscribers_count, monthly_revenue_etb=monthly_revenue_etb,
        asking_price_etb=asking_price_etb, description=description, handle=handle,
        proof_image_url=save_proof_image(proof_image),
        status=ListingStatus.Pending_Review,  # always reviewed (or bot-verified) before going public
    )
    db.add(listing)
    db.commit()
    return listing_out(listing, detail=True)


@app.get("/listings")
def list_listings(
    platform: PlatformType | None = None, category: str | None = None,
    min_price: float | None = None, max_price: float | None = None,
    q: str | None = None, sort: Literal["new", "price_asc", "price_desc", "followers"] = "new",
    limit: int = 30, offset: int = 0, db: Session = Depends(get_db),
):
    stmt = select(Listing).where(Listing.status == ListingStatus.Active)
    if platform:
        stmt = stmt.where(Listing.platform_type == platform)
    if category:
        stmt = stmt.where(Listing.category == category)
    if min_price is not None:
        stmt = stmt.where(Listing.asking_price_etb >= min_price)
    if max_price is not None:
        stmt = stmt.where(Listing.asking_price_etb <= max_price)
    if q:
        stmt = stmt.where(Listing.account_title.ilike(f"%{q}%"))
    order = {"new": Listing.created_at.desc(), "price_asc": Listing.asking_price_etb.asc(),
             "price_desc": Listing.asking_price_etb.desc(), "followers": Listing.followers_subscribers_count.desc()}[sort]
    rows = db.scalars(stmt.order_by(order).limit(min(limit, 100)).offset(offset)).all()
    return [listing_out(l) for l in rows]


@app.get("/listings/{listing_id}")
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    l = db.get(Listing, listing_id)
    if not l or l.status not in (ListingStatus.Active, ListingStatus.Sold):
        raise HTTPException(404, "Listing not found")
    return listing_out(l, detail=True)


@app.get("/archive")
def sold_archive(limit: int = 30, db: Session = Depends(get_db)):
    """Social proof: completed deals with identifying details masked."""
    rows = db.execute(
        select(Listing, EscrowTransaction)
        .join(EscrowTransaction, EscrowTransaction.listing_id == Listing.id)
        .where(EscrowTransaction.status == EscrowStatus.Completed)
        .order_by(EscrowTransaction.released_at.desc()).limit(min(limit, 100))
    ).all()
    out = []
    for l, tx in rows:
        t = l.account_title
        f = l.followers_subscribers_count
        bucket = "100K+" if f >= 100_000 else "10K+" if f >= 10_000 else "1K+" if f >= 1_000 else "<1K"
        out.append({
            "platform_type": l.platform_type.value, "category": l.category,
            "masked_title": (t[:1] + "*" * min(len(t) - 1, 8)) if t else "***",
            "followers_bucket": bucket, "sold_price_etb": float(tx.agreed_amount_etb),
            "completed_on": tx.released_at.date().isoformat() if tx.released_at else None,
        })
    return out


@app.get("/me/listings")
def my_listings(user: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(Listing).where(Listing.seller_id == user.id).order_by(Listing.created_at.desc())).all()
    return [listing_out(l) for l in rows]


# ----------------------------------------------------------------------------- escrow workflow
def get_tx(db: Session, tx_id: int, user: User, roles=("buyer", "seller")) -> EscrowTransaction:
    tx = db.scalar(select(EscrowTransaction).where(EscrowTransaction.id == tx_id).with_for_update())
    allowed = tx and ((("buyer" in roles) and tx.buyer_id == user.id) or (("seller" in roles) and tx.seller_id == user.id))
    if not tx or not (allowed or user.is_admin):
        raise HTTPException(404, "Deal not found")
    return tx


def require_status(tx: EscrowTransaction, *statuses: EscrowStatus):
    if tx.status not in statuses:
        raise HTTPException(409, f"Deal is '{tx.status.value}'; this action is not allowed now")


def complete_deal(db: Session, tx: EscrowTransaction):
    """Release funds to the seller (minus 2% commission). Call only from validated states."""
    tx.status = EscrowStatus.Completed
    tx.released_at = utcnow()
    tx.payout_amount_etb = tx.agreed_amount_etb - tx.commission_fee_etb
    tx.listing.status = ListingStatus.Sold
    # TODO: trigger the real payout here (Telebirr / CBE Birr / Chapa disbursement API) and store its reference.


@app.post("/escrow", status_code=201)
def create_escrow(body: EscrowIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    listing = db.scalar(select(Listing).where(Listing.id == body.listing_id).with_for_update())
    if not listing or listing.status != ListingStatus.Active:
        raise HTTPException(404, "Listing is not available")
    if listing.seller_id == user.id:
        raise HTTPException(400, "You cannot buy your own listing")
    busy = db.scalar(select(EscrowTransaction.id).where(EscrowTransaction.listing_id == listing.id,
                                                        EscrowTransaction.status.in_(OPEN_ESCROW_STATUSES)))
    if busy:
        raise HTTPException(409, "Another deal is already in progress for this listing")
    days = body.cooldown_days or DEFAULT_COOLDOWN_DAYS[listing.platform_type.value]
    tx = EscrowTransaction(
        listing_id=listing.id, buyer_id=user.id, seller_id=listing.seller_id,
        agreed_amount_etb=body.agreed_amount_etb, commission_fee_etb=calc_commission(body.agreed_amount_etb),
        cooldown_days=days, payment_reference=f"AP-{secrets.token_hex(4).upper()}",
    )
    db.add(tx)
    db.commit()
    return escrow_out(tx)


@app.get("/escrow")
def my_deals(user: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(EscrowTransaction)
                      .where(or_(EscrowTransaction.buyer_id == user.id, EscrowTransaction.seller_id == user.id))
                      .order_by(EscrowTransaction.created_at.desc())).all()
    return [escrow_out(t) for t in rows]


@app.post("/escrow/{tx_id}/confirm-deposit")
def confirm_deposit(tx_id: int, _: User = Depends(admin_user), db: Session = Depends(get_db)):
    """Admin (or a verified payment webhook) confirms the buyer's money reached the escrow vault."""
    tx = db.scalar(select(EscrowTransaction).where(EscrowTransaction.id == tx_id).with_for_update())
    if not tx:
        raise HTTPException(404, "Deal not found")
    require_status(tx, EscrowStatus.Pending_Deposit)
    tx.status = EscrowStatus.Secured_in_Escrow
    db.commit()
    return escrow_out(tx)


@app.post("/escrow/{tx_id}/credentials-transferred")
def credentials_transferred(tx_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)):
    tx = get_tx(db, tx_id, user, roles=("seller",))
    if tx.seller_id != user.id:
        raise HTTPException(403, "Only the seller can do this")
    require_status(tx, EscrowStatus.Secured_in_Escrow)
    tx.status = EscrowStatus.Credentials_Transferred
    db.commit()
    return escrow_out(tx)


@app.post("/escrow/{tx_id}/confirm-access")
def confirm_access(tx_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)):
    """Buyer confirms they can log in. This starts the mandatory 3-7 day anti-recovery-scam cooldown."""
    tx = get_tx(db, tx_id, user, roles=("buyer",))
    if tx.buyer_id != user.id:
        raise HTTPException(403, "Only the buyer can do this")
    require_status(tx, EscrowStatus.Credentials_Transferred)
    tx.status = EscrowStatus.Buyer_Verification_Period
    tx.cooldown_ends_at = utcnow() + timedelta(days=tx.cooldown_days)
    db.commit()
    return escrow_out(tx)


@app.post("/escrow/{tx_id}/dispute")
def open_dispute(tx_id: int, body: DisputeIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    tx = get_tx(db, tx_id, user)
    if user.id not in (tx.buyer_id, tx.seller_id):
        raise HTTPException(403, "Only the buyer or seller can open a dispute")
    require_status(tx, EscrowStatus.Secured_in_Escrow, EscrowStatus.Credentials_Transferred,
                   EscrowStatus.Buyer_Verification_Period)
    tx.status = EscrowStatus.Disputed  # funds frozen: the cooldown worker only releases Buyer_Verification_Period deals
    tx.dispute_reason = f"[{'buyer' if user.id == tx.buyer_id else 'seller'}] {body.reason}"
    db.commit()
    return escrow_out(tx)


# --- in-app chat with anti-bypass scanning
BYPASS_PATTERNS = [
    (re.compile(r"(\+?251|\b0)[79]\d{8}\b"), "phone number"),
    (re.compile(r"(t\.me/|telegram\.me/|wa\.me/|@[A-Za-z][\w]{4,})", re.I), "telegram/whatsapp handle"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "email address"),
    (re.compile(r"\b(whatsapp|signal|imo|outside (the )?(app|platform)|off[- ]platform|directly|"
                r"pay me|send (me )?(money|birr)|telebirr|cbe ?birr|bank transfer)\b", re.I), "off-platform wording"),
    (re.compile(r"(ከመድረክ ውጭ|ከመድረኩ ውጪ|በቀጥታ|ስልኬ|ቴሌብር|ባንክ ቁጥር)"), "off-platform wording (Amharic)"),
]


def scan_bypass(text: str) -> str | None:
    for pattern, reason in BYPASS_PATTERNS:
        if pattern.search(text):
            return reason
    return None


@app.post("/escrow/{tx_id}/messages", status_code=201)
def post_message(tx_id: int, body: MessageIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    tx = get_tx(db, tx_id, user)
    if user.id not in (tx.buyer_id, tx.seller_id):
        raise HTTPException(403, "Only deal participants can chat")
    reason = scan_bypass(body.body)
    msg = DealMessage(escrow_id=tx.id, sender_id=user.id, body=body.body, flagged=bool(reason), flag_reason=reason)
    db.add(msg)
    if reason:
        user.bypass_flag_count += 1
        if user.bypass_flag_count >= 3:
            user.is_flagged = True
    db.commit()
    return {"id": msg.id, "flagged": msg.flagged,
            "warning": "Contact details and off-platform payments are not allowed. This was logged." if reason else None}


@app.get("/escrow/{tx_id}/messages")
def get_messages(tx_id: int, user: User = Depends(current_user), db: Session = Depends(get_db)):
    tx = get_tx(db, tx_id, user)
    msgs = db.scalars(select(DealMessage).where(DealMessage.escrow_id == tx.id).order_by(DealMessage.id)).all()
    out = []
    for m in msgs:
        hide = m.flagged and not user.is_admin and m.sender_id != user.id  # counterpart never sees flagged content
        out.append({"id": m.id, "sender_id": m.sender_id, "created_at": m.created_at.isoformat(), "flagged": m.flagged,
                    "body": "[hidden: contact details are not allowed]" if hide else m.body})
    return out


# ----------------------------------------------------------------------------- admin tools
@app.get("/admin/listings")
def admin_listings(status: ListingStatus = ListingStatus.Pending_Review, _: User = Depends(admin_user),
                   db: Session = Depends(get_db)):
    rows = db.scalars(select(Listing).where(Listing.status == status).order_by(Listing.created_at)).all()
    return [{**listing_out(l, detail=True), "handle": l.handle} for l in rows]


@app.post("/admin/listings/{listing_id}/{action}")
def admin_listing_action(listing_id: int, action: Literal["approve", "suspend"], _: User = Depends(admin_user),
                         db: Session = Depends(get_db)):
    l = db.get(Listing, listing_id)
    if not l:
        raise HTTPException(404, "Listing not found")
    if l.status == ListingStatus.Sold:
        raise HTTPException(409, "Sold listings cannot be changed")
    l.status = ListingStatus.Active if action == "approve" else ListingStatus.Suspended
    db.commit()
    return listing_out(l)


@app.get("/admin/deposits")
def admin_deposits(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(EscrowTransaction).where(EscrowTransaction.status == EscrowStatus.Pending_Deposit)
                      .order_by(EscrowTransaction.created_at)).all()
    return [escrow_out(t) for t in rows]


@app.get("/admin/disputes")
def admin_disputes(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(EscrowTransaction).where(EscrowTransaction.status == EscrowStatus.Disputed)
                      .order_by(EscrowTransaction.updated_at)).all()
    return [escrow_out(t) for t in rows]


@app.post("/admin/escrow/{tx_id}/freeze")
def admin_freeze(tx_id: int, body: DisputeIn, admin: User = Depends(admin_user), db: Session = Depends(get_db)):
    """Admin-initiated freeze (e.g. after anti-bypass flags or a suspected recovery attempt)."""
    tx = db.scalar(select(EscrowTransaction).where(EscrowTransaction.id == tx_id).with_for_update())
    if not tx:
        raise HTTPException(404, "Deal not found")
    require_status(tx, EscrowStatus.Secured_in_Escrow, EscrowStatus.Credentials_Transferred,
                   EscrowStatus.Buyer_Verification_Period)
    tx.status = EscrowStatus.Disputed
    tx.dispute_reason = f"[admin #{admin.id}] {body.reason}"
    db.commit()
    return escrow_out(tx)


@app.post("/admin/escrow/{tx_id}/resolve")
def admin_resolve(tx_id: int, body: ResolveIn, _: User = Depends(admin_user), db: Session = Depends(get_db)):
    tx = db.scalar(select(EscrowTransaction).where(EscrowTransaction.id == tx_id).with_for_update())
    if not tx:
        raise HTTPException(404, "Deal not found")
    require_status(tx, EscrowStatus.Disputed)
    tx.resolution_note = body.note
    if body.outcome == "release_to_seller":
        complete_deal(db, tx)
    else:
        tx.status = EscrowStatus.Refunded  # full refund incl. commission; trigger refund payout here
    db.commit()
    return escrow_out(tx)


@app.get("/admin/flags")
def admin_flags(_: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(DealMessage).where(DealMessage.flagged).order_by(DealMessage.id.desc()).limit(100)).all()
    users = db.scalars(select(User).where(User.bypass_flag_count > 0).order_by(User.bypass_flag_count.desc())).all()
    return {
        "users": [{"id": u.id, "full_name": u.full_name, "flags": u.bypass_flag_count, "is_flagged": u.is_flagged} for u in users],
        "messages": [{"id": m.id, "escrow_id": m.escrow_id, "sender_id": m.sender_id, "body": m.body,
                      "reason": m.flag_reason, "created_at": m.created_at.isoformat()} for m in rows],
    }


@app.post("/admin/users/{user_id}/verify")
def admin_verify_user(user_id: int, _: User = Depends(admin_user), db: Session = Depends(get_db)):
    u = db.get(User, user_id)
    if not u:
        raise HTTPException(404, "User not found")
    u.is_verified = True
    db.commit()
    return me_out(u)


# ----------------------------------------------------------------------------- Telegram bot endpoints
@app.post("/bot/listings", status_code=201, dependencies=[Depends(bot_auth)])
def bot_create_listing(body: BotListingIn, db: Session = Depends(get_db)):
    """Called by telegram_bot.py after it verified channel ownership and measured quality."""
    seller = db.scalar(select(User).where(User.telegram_id == body.telegram_id))
    if not seller:
        raise HTTPException(404, "No Amalaj Plus account is linked to this Telegram ID")
    quality = None if body.fake_followers_score is None else max(0, min(100, round(100 - body.fake_followers_score)))
    publish = body.bot_verified and quality is not None and quality >= 60
    listing = Listing(
        seller_id=seller.id, platform_type=PlatformType.Telegram, account_title=body.account_title,
        category=body.category, followers_subscribers_count=body.followers_subscribers_count,
        monthly_revenue_etb=body.monthly_revenue_etb, asking_price_etb=body.asking_price_etb,
        description=body.description, handle=body.handle, engagement_rate=body.engagement_rate,
        quality_score=quality, status=ListingStatus.Active if publish else ListingStatus.Pending_Review,
    )
    db.add(listing)
    db.flush()
    db.add(VerificationLog(listing_id=listing.id, bot_verified=body.bot_verified,
                           fake_followers_score=body.fake_followers_score))
    db.commit()
    return {"listing_id": listing.id, "status": listing.status.value, "quality_score": quality}


@app.get("/bot/users/{telegram_id}", dependencies=[Depends(bot_auth)])
def bot_user_lookup(telegram_id: int, db: Session = Depends(get_db)):
    u = db.scalar(select(User).where(User.telegram_id == telegram_id))
    if not u:
        raise HTTPException(404, "Not linked")
    return me_out(u)
