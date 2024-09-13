from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security.security import get_db, admin_only
from app.models.models import Category
from app.schemas.category import CategoryBase

router = APIRouter(tags=["categories"])


@router.get("/categories", response_model=List[CategoryBase])
async def get_all_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


@router.get("/categories/{category_id}", response_model=CategoryBase)
async def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(category_id == Category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found")
    return db_category


@router.post("/categories/create", response_model=CategoryBase, dependencies=[Depends(admin_only)])
async def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    new_category = Category(name=category.name, description=category.description)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.put("/categories/{category_id}", response_model=CategoryBase, dependencies=[Depends(admin_only)])
async def update_category(category_id: int, category: CategoryBase, db: Session = Depends(get_db)):
    category_to_update = db.query(Category).filter(category_id == Category.id).first()
    if category_to_update is None:
        raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found")
    category_to_update.name = category.name
    category_to_update.description = category.description
    db.commit()
    db.refresh(category_to_update)
    return category_to_update


@router.delete("/categories/{category_id}", dependencies=[Depends(admin_only)])
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_to_delete = db.query(Category).filter(category_id == Category.id).first()
    if category_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found")
    db.delete(category_to_delete)
    db.commit()
    return {"message": f"Category with id {category_id} deleted successfully"}
