from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str | None