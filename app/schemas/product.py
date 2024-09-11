from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str | None
    price: float
    stock: int

class Product(ProductBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

