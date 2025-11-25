from pydantic import BaseModel
from uuid import UUID


class DishForCatalogSchema(BaseModel):
    id: UUID
    name: str
    description: str
    img: str
    total_ingredients: int
