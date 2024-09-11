from pydantic import BaseModel
from app.schemas.product import Product

class UserBase(BaseModel):
    email: str
    full_name: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True