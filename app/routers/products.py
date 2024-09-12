from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security.security import get_db, get_current_user, admin_only
from app.models.models import Product, User
from app.schemas.product import ProductCreate, ProductBase

router = APIRouter()


@router.post("/products/create", response_model=ProductBase)
async def create_product(product: ProductCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(admin_only)):
    new_product = Product(name=product.name, description=product.description, price=product.price, stock=product.stock,
                          category=product.category, user_id=current_user.id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products", response_model=List[ProductBase])
async def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/products/{product_id}", response_model=ProductBase)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(product_id == Product.id).first()

@router.put("/products/{product_id}", response_model=ProductBase)
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(admin_only)):
    product_to_update = db.query(Product).filter(product_id == Product.id).first()
    product_to_update.name = product.name
    product_to_update.description = product.description
    product_to_update.price = product.price
    product_to_update.stock = product.stock
    product_to_update.category = product.category
    db.commit()
    db.refresh(product_to_update)
    return product_to_update

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(admin_only)):
    product_to_delete = db.query(Product).filter(product_id == Product.id).first()
    db.delete(product_to_delete)
    db.commit()
    return {"message": "Product deleted successfully"}