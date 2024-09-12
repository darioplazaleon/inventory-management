from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from app.core.security.security import get_db, get_password_hash, authenticate_user
from app.core.security.tokenJWT import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.models.models import User
from app.schemas.token import Token
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

@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, user_id=user.id, role=user.role.name, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

