from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security.security import get_db, get_password_hash
from app.models.models import User
from app.schemas.user import UserCreate, UserBase

router = APIRouter()

@router.post("/register", response_model=UserBase)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(user.email == User.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)

    new_user = User(email=user.email, hashed_password=hashed_password,full_name=user.full_name)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
