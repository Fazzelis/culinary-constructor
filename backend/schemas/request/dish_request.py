from pydantic import BaseModel
from uuid import UUID
from schemas.request.recipe_step_request import RecipeStepWithoutDishIdSchema


class DishRequestSchema(BaseModel):
    name: str
    description: str
    img_id: UUID
    ingredients: dict[UUID, str]
    recipe_steps: list[RecipeStepWithoutDishIdSchema]
