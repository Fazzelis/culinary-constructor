from pydantic import BaseModel
from uuid import UUID


class RecipeStepRequest(BaseModel):
    step_number: int
    description: str
    dish_id: UUID
