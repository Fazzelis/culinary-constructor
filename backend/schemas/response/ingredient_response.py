from pydantic import BaseModel
from uuid import UUID


class IngredientResponseSchema(BaseModel):
    id: UUID
    name: str
    category_id: UUID
