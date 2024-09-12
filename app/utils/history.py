from app.models.models import ProductHistory


def log_product_operation(db, product_id: int, operation: str, user_id: int):
    new_log = ProductHistory(product_id=product_id, operation=operation, user_id=user_id)
    db.add(new_log)
    db.commit()