from pydantic import BaseModel
from uuid import UUID
from schemas.response.ingredient_response import IngredientForCategoryResponseSchema


class CategoryResponseSchema(BaseModel):
    id: UUID
    name: str
    color_id: UUID


class CategoryWithoutColorIdResponseSchema(BaseModel):
    id: UUID
    name: str


class CategoriesResponseSchema(BaseModel):
    categories: list[CategoryWithoutColorIdResponseSchema]


class DeleteCategoryResponseSchema(BaseModel):
    id: UUID
    row_count: int


class CategoryIngredientsResponseSchema(BaseModel):
    color: str
    ingredients: list[IngredientForCategoryResponseSchema]
