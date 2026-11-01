from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
import os
import re
import shutil

from ..database import SessionLocal
from ..models import User

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def is_valid_ethiopian_phone(phone: str) -> bool:
    clean_phone = phone.strip()
    
    # 1. ርዝመቱ በትክክል 10 አሃዝ (ለ 09/07) ወይም 13 አሃዝ (ለ +251) መሆኑን ማረጋገጥ
    if not (clean_phone.isdigit() or (clean_phone.startswith('+') and clean_phone[1:].isdigit())):
        return False
        
    # 2. የኢትዮጵያ ስልክ ቁጥር ትክክለኛ ቅንብር (09 ወይም 07 በ 8 ተጨማሪ አሃዞች)
    pattern = r"^(?:\+2519|\+2517|09|07)\d{8}$"
    if not re.match(pattern, clean_phone):
        return False
        
    # 3. እንደ 0000000000 ወይም 1111111111 ያሉ ተደጋጋሚ የውሸት ቁጥሮችን በጽኑ ማገድ
    core_digits = clean_phone[-9:] # የመጨረሻዎቹን 9 አሃዞች መውሰድ
    if len(set(core_digits)) <= 1:
        return False
        
    return True

@router.post("/verify")
async def verify_seller(
    full_name: str = Form(...),
    mother_name: str = Form(...),
    phone: str = Form(...),
    fayida_num: str = Form(...),
    id_front: UploadFile = File(...),
    id_back: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # ስልክ ቁጥሩን በጥብቅ ማረጋገጥ
    if not is_valid_ethiopian_phone(phone):
        raise HTTPException(
            status_code=400,
            detail="ስህተት: ያስገቡት ስልክ ቁጥር ትክክለኛ የኢትዮጵያ ስልክ ቁጥር አይደለም (09 ወይም 07 ብቻ)!"
        )

    # የፋይዳ ቁጥር (16 አሃዝ እና ሁሉም ዜሮ ወይም አንድ አይነት ቁጥር መሆን የለባቸውም)
    if len(fayida_num) != 16 or not fayida_num.isdigit() or len(set(fayida_num)) <= 1:
        raise HTTPException(
            status_code=400,
            detail="ስህተት: የፋይዳ መታወቂያ ቁጥር በትክክል 16 ልዩ አሃዞች መሆን አለበት!"
        )

    # ዱፕሊኬት ቼክ
    existing_user = db.query(User).filter(User.phone_number == phone.strip()).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="ስህተት: ይህ ስልክ ቁጥር ቀደም ብሎ ተመዝግቧል!"
        )

    # ፎቶዎችን ማስቀመጥ
    os.makedirs("uploads", exist_ok=True)
    front_path = f"uploads/{phone}_front_{id_front.filename}"
    back_path = f"uploads/{phone}_back_{id_back.filename}"

    with open(front_path, "wb") as buffer:
        shutil.copyfileobj(id_front.file, buffer)
    with open(back_path, "wb") as buffer:
        shutil.copyfileobj(id_back.file, buffer)

    # ተጠቃሚውን መመዝገብ
    new_user = User(
        full_name=full_name.strip(),
        phone_number=phone.strip(),
        password_hash="verified_secure",
        is_verified=True,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "status": "success",
        "message": "ማረጋገጫው ተሳክቷል!",
    }