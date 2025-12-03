from pydantic import BaseModel
from uuid import UUID


class IngredientSchema(BaseModel):
    id: UUID
    name: str
    count: str
