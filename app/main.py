from fastapi import FastAPI

from app.routers import users, products, exports, categories
from app.models import models
from app.db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(exports.router)
app.include_router(categories.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
