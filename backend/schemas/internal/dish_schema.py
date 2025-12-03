from pydantic import BaseModel
from uuid import UUID


class DishForCatalogSchema(BaseModel):
    id: UUID
    name: str
    description: str
    cooking_time: str
    img: str
    total_ingredients: int


class CaloriesSchema(BaseModel):
    name: str
    counterNum: int
    counterText: str
