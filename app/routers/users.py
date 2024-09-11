from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserBase, UserInDB

router = APIRouter()

@router.post("/register")
async def register(user: UserBase):
    return user

