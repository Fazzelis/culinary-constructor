from pydantic import BaseModel
from uuid import UUID


class RecipeSchema(BaseModel):
    id: UUID
    step_number: int
    description: str

    class Config:
        from_attributes = True
