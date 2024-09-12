from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security.security import get_db, get_current_user, admin_only
from app.models.models import Product, User, Category
from app.schemas.product import ProductCreate, ProductBase

router = APIRouter(tags=["products"])


@router.post("/products/create", response_model=ProductBase)
async def create_product(product: ProductCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(admin_only)):
    categories_db = db.query(Category).filter(Category.id.in_(product.category_ids)).all()
    new_product = Product(name=product.name, description=product.description, price=product.price, stock=product.stock,
                          categories=categories_db, user_id=current_user.id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/products", response_model=List[ProductBase])
async def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/products/{product_id}", response_model=ProductBase)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductBase)
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db),
                         current_user: User = Depends(admin_only)):
    product_to_update = db.query(Product).filter(product_id == Product.id).first()
    if product_to_update is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
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
    if product_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    db.delete(product_to_delete)
    db.commit()
    return {"message": f"Product with id {product_id} deleted successfully"}


@router.get("/products/category/{category}", response_model=List[ProductBase])
async def get_products_by_category(category: int, db: Session = Depends(get_db)):
    db_products = db.query(Product).join(Product.categories).filter(category == Category.id).all()
    if db_products is None:
        raise HTTPException(status_code=404, detail=f"Products with category {category} not found")
    return db_products
