from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security.security import get_db
from app.models.models import Product
from app.utils.transform import export_products_to_csv, export_products_to_json, export_products_to_pdf

router = APIRouter(tags=["Export"])


@router.get("/export-csv/all-products")
async def export_all_products_to_csv(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")

    return export_products_to_csv(products, filename="products")


@router.get("/export-csv/low-stock")
async def export_low_stock_products_to_csv(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.stock < 100).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products with low stock found")

    return export_products_to_csv(products, filename="products_low_stock")


@router.get("/export-json/all-products")
async def export_all_products_to_json(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")

    return export_products_to_json(products, filename="products")

@router.get("/export-json/low-stock")
async def export_low_stock_products_to_json(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.stock < 100).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products with low stock found")

    return export_products_to_json(products, filename="products_low_stock")

@router.get("/export-pdf/all-products")
async def export_all_products_to_pdf(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")

    return export_products_to_pdf(products, filename="products")

@router.get("/export-pdf/low-stock")
async def export_low_stock_products_to_pdf(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.stock < 100).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products with low stock found")

    return export_products_to_pdf(products, filename="products_low_stock")