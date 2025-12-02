from pydantic import BaseModel
from uuid import UUID
from schemas.internal.ingredient_schema import IngredientSchema
from schemas.internal.recipe_schema import RecipeSchema
from schemas.internal.dish_schema import DishForCatalogSchema
from schemas.internal.pagination_schema import PaginationSchema


class DishResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str
    img: str
    protein: int | None = None
    fats: int | None = None
    carbs: int | None = None
    calories: int | None = None
    ingredients: list[IngredientSchema]
    recipe_steps: list[RecipeSchema]


class DishesResponseSchema(BaseModel):
    pagination: PaginationSchema
    dishes: list[DishForCatalogSchema]
