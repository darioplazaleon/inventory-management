# # init_db.py
# from sqlalchemy.orm import Session
# from app.db.database import SessionLocal
# from app.models.models import User, Category
# from app.core.security.security import get_password_hash
#
# def init_db():
#     db: Session = SessionLocal()
#
#     # Crear usuarios
#     user1 = User(
#         email="dario@gmail.com",
#         hashed_password=get_password_hash("4102002"),
#         full_name="Dario Alessandro Plaza Leon",
#         role="ADMIN"
#     )
#     user2 = User(
#         email="agus@gmail.com",
#         hashed_password=get_password_hash("4102002"),
#         full_name="Agustin Plaza Leon",
#         role="USER"
#     )
#
#     db.add(user1)
#     db.add(user2)
#
#     # Crear categorías
#     category1 = Category(
#         name="Electronics",
#         description="Electronic items"
#     )
#     category2 = Category(
#         name="Books",
#         description="Various kinds of books"
#     )
#     category3 = Category(
#         name="Clothing",
#         description="Clothing items"
#     )
#     category4 = Category(
#         name="Home",
#         description="Home items"
#     )
#
#     db.add(category1)
#     db.add(category2)
#     db.add(category3)
#     db.add(category4)
#
#     db.commit()
#     db.close()
