from pydantic import BaseModel
from uuid import UUID
from schemas.response.ingredient_response import IngredientForCategoryResponseSchema


class CategoryResponseSchema(BaseModel):
    id: UUID
    name: str
    color_id: UUID


class CategoriesResponseSchema(BaseModel):
    categories: list[CategoryResponseSchema]


class DeleteCategoryResponseSchema(BaseModel):
    id: UUID
    row_count: int


class CategoryIngredientsResponseSchema(BaseModel):
    color: str
    ingredients: list[IngredientForCategoryResponseSchema]
