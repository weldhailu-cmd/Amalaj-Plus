from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from decimal import Decimal

from ..database import SessionLocal
from ..models import Listing, ListingStatus, PlatformType, User

router = APIRouter(prefix="/api/v1", tags=["Marketplace"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ListingCreate(BaseModel):
    title: str
    platform: str
    subscribers: str
    views: str
    price: str
    description: str = ""

@router.get("/marketplace")
def get_marketplace_listings(db: Session = Depends(get_db)):
    listings = db.query(Listing).all()
    if not listings:
        return [
            {"id": 1, "title": "Crypto Hub", "platform": "Telegram", "subscribers": "12K", "views": "45K", "price": "15,000 ETB"},
            {"id": 2, "title": "Sportsphere", "platform": "YouTube", "subscribers": "303K", "views": "14M", "price": "78,000 ETB"},
        ]
    return [
        {
            "id": l.id,
            "title": l.account_title,
            "platform": l.platform_type.value,
            "subscribers": str(l.followers_subscribers_count),
            "views": "Verified",
            "price": f"{l.asking_price_etb} ETB"
        } for l in listings
    ]

@router.post("/marketplace/create")
def create_listing(data: ListingCreate, db: Session = Depends(get_db)):
    try:
        seller = db.query(User).first()
        if not seller:
            seller = User(full_name="Verified Seller", phone_number="0911000000", password_hash="dummy", is_verified=True)
            db.add(seller)
            db.commit()
            db.refresh(seller)

        plat_map = {
            "Telegram": PlatformType.Telegram,
            "YouTube": PlatformType.YouTube,
            "TikTok": PlatformType.TikTok,
            "Instagram": PlatformType.Instagram,
            "Facebook": PlatformType.Facebook
        }
        p_type = plat_map.get(data.platform, PlatformType.Telegram)

        clean_sub = ''.join(filter(str.isdigit, data.subscribers))
        sub_count = int(clean_sub) if clean_sub else 1000

        clean_price = data.price.replace(",", "").replace("ETB", "").strip()
        price_val = Decimal(clean_price) if clean_price.replace('.', '', 1).isdigit() else Decimal("1000.00")

        new_listing = Listing(
            seller_id=seller.id,
            account_title=data.title,
            platform_type=p_type,
            category="General",
            followers_subscribers_count=sub_count,
            asking_price_etb=price_val,
            description=data.description,
            status=ListingStatus.Active
        )
        db.add(new_listing)
        db.commit()
        db.refresh(new_listing)
        return {"status": "success", "message": "ማስታወቂያዎ በተሳካ ሁኔታ ተለጠፈ!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))