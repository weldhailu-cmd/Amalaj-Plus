"""
models.py - አማላጅ ፕላስ (Amalaj Plus) database schema (SQLAlchemy 2.0).

All timestamps are naive UTC. Money is stored as Numeric(14, 2) in ETB.
Works on SQLite (dev) and PostgreSQL (prod): set DATABASE_URL.
"""
import enum
import os
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP

from sqlalchemy import (
    BigInteger, Boolean, DateTime, Enum, Float, ForeignKey, Index, Integer,
    Numeric, String, Text, create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

COMMISSION_RATE = Decimal("0.02")  # strictly 2% of the agreed price


def utcnow() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


def calc_commission(amount: Decimal) -> Decimal:
    """2% platform fee, rounded to the nearest cent (ETB santim)."""
    return (Decimal(amount) * COMMISSION_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class PlatformType(str, enum.Enum):
    TikTok = "TikTok"
    YouTube = "YouTube"
    Telegram = "Telegram"
    Instagram = "Instagram"
    Facebook = "Facebook"
    X_Twitter = "X_Twitter"
    Website_SaaS = "Website_SaaS"


class ListingStatus(str, enum.Enum):
    Active = "Active"
    Pending_Review = "Pending_Review"
    Sold = "Sold"
    Suspended = "Suspended"


class EscrowStatus(str, enum.Enum):
    Pending_Deposit = "Pending_Deposit"
    Secured_in_Escrow = "Secured_in_Escrow"
    Credentials_Transferred = "Credentials_Transferred"
    Buyer_Verification_Period = "Buyer_Verification_Period"
    Completed = "Completed"
    Disputed = "Disputed"
    Refunded = "Refunded"


OPEN_ESCROW_STATUSES = (
    EscrowStatus.Pending_Deposit,
    EscrowStatus.Secured_in_Escrow,
    EscrowStatus.Credentials_Transferred,
    EscrowStatus.Buyer_Verification_Period,
    EscrowStatus.Disputed,
)


def _enum(e):  # store as plain strings, no native DB enum (easier migrations)
    return Enum(e, native_enum=False, length=32, validate_strings=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(120))
    phone_number: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    telegram_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, index=True)
    email: Mapped[str | None] = mapped_column(String(160), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(300))
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    # operational fields beyond the base spec
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    bypass_flag_count: Mapped[int] = mapped_column(Integer, default=0)
    is_flagged: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)

    listings: Mapped[list["Listing"]] = relationship(back_populates="seller")


class Listing(Base):
    __tablename__ = "listings"
    __table_args__ = (Index("ix_listing_status_platform", "status", "platform_type"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    platform_type: Mapped[PlatformType] = mapped_column(_enum(PlatformType))
    account_title: Mapped[str] = mapped_column(String(160))
    category: Mapped[str] = mapped_column(String(80))
    followers_subscribers_count: Mapped[int] = mapped_column(Integer)
    monthly_revenue_etb: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    asking_price_etb: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    description: Mapped[str] = mapped_column(Text, default="")
    proof_image_url: Mapped[str | None] = mapped_column(String(300))
    status: Mapped[ListingStatus] = mapped_column(_enum(ListingStatus), default=ListingStatus.Pending_Review)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)
    # extras
    handle: Mapped[str | None] = mapped_column(String(160))          # @channel / profile URL (never shown publicly)
    engagement_rate: Mapped[float | None] = mapped_column(Float)     # percent
    quality_score: Mapped[int | None] = mapped_column(Integer)       # 0-100, "Verified Quality Score"

    seller: Mapped[User] = relationship(back_populates="listings")
    verification_logs: Mapped[list["VerificationLog"]] = relationship(back_populates="listing")


class EscrowTransaction(Base):
    __tablename__ = "escrow_transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.id"), index=True)
    buyer_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    agreed_amount_etb: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    commission_fee_etb: Mapped[Decimal] = mapped_column(Numeric(14, 2))  # 2% of agreed amount
    status: Mapped[EscrowStatus] = mapped_column(_enum(EscrowStatus), default=EscrowStatus.Pending_Deposit, index=True)
    cooldown_ends_at: Mapped[datetime | None] = mapped_column(DateTime, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow, onupdate=utcnow)
    # extras
    cooldown_days: Mapped[int] = mapped_column(Integer, default=7)  # 3..7
    payment_reference: Mapped[str | None] = mapped_column(String(80))
    dispute_reason: Mapped[str | None] = mapped_column(Text)
    resolution_note: Mapped[str | None] = mapped_column(Text)
    payout_amount_etb: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    released_at: Mapped[datetime | None] = mapped_column(DateTime)

    listing: Mapped[Listing] = relationship()
    buyer: Mapped[User] = relationship(foreign_keys=[buyer_id])
    seller: Mapped[User] = relationship(foreign_keys=[seller_id])


class VerificationLog(Base):
    __tablename__ = "verification_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.id"), index=True)
    bot_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    fake_followers_score: Mapped[float | None] = mapped_column(Float)  # 0 (clean) .. 100 (mostly fake)
    checked_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)

    listing: Mapped[Listing] = relationship(back_populates="verification_logs")


class DealMessage(Base):
    """In-app deal chat. Every message is logged and scanned for off-platform contact attempts."""
    __tablename__ = "deal_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    escrow_id: Mapped[int] = mapped_column(ForeignKey("escrow_transactions.id"), index=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    body: Mapped[str] = mapped_column(Text)
    flagged: Mapped[bool] = mapped_column(Boolean, default=False)
    flag_reason: Mapped[str | None] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./amalaj.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def init_db() -> None:
    Base.metadata.create_all(engine)
