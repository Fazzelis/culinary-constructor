from pydantic import BaseModel
from uuid import UUID


class IngredientRequestSchema(BaseModel):
    name: str
    category_id: UUID
