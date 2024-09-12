from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str | None
    price: float
    stock: int


class ProductCreate(ProductBase):
    category_ids: List[int]


class Product(ProductBase):
    id: int
    owner_id: int
    categories: List[int]

    class Config:
        orm_mode = True
