from pydantic import BaseModel
from uuid import UUID
from schemas.internal.ingredient_schema import IngredientSchema
from schemas.internal.recipe_schema import RecipeSchema


class DishResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str
    img: str
    ingredients: list[IngredientSchema]
    recipe_steps: list[RecipeSchema]
