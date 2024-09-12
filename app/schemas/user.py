from pydantic import BaseModel
from app.schemas.product import Product
from app.models.roles import Role

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    email: str
    full_name: str
    password: str

class UserInDB(UserBase):
    id: int
    hashed_password: str
    role: Role

class User(UserBase):
    id: int
    role: Role
    products: list[Product] = []

    class Config:
        orm_mode = True