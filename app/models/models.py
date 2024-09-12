from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float, Table, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.roles import Role

product_category = Table(
    "product_category",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    role = Column(Enum(Role), default=Role.USER)

    history = relationship("ProductHistory", back_populates="user")
    products = relationship("Product", back_populates="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    history = relationship("ProductHistory", back_populates="product")
    categories = relationship("Category", secondary=product_category, back_populates="products")
    owner = relationship("User", back_populates="products")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    products = relationship("Product", secondary=product_category, back_populates="categories")


class ProductHistory(Base):
    __tablename__ = "product_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    operation = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    user_id = Column(Integer, ForeignKey("users.id"))

    product = relationship("Product", back_populates="history")
    user = relationship("User", back_populates="history")
