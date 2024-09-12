from pydantic import BaseModel

from app.models.categories import Category


class ProductBase(BaseModel):
    name: str
    description: str | None
    price: float
    stock: int
    category: Category

class ProductCreate(ProductBase):
    name: str
    description: str | None
    price: float
    stock: int
    category: Category

class Product(ProductBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True