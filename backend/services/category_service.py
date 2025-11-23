from sqlalchemy.ext.asyncio import AsyncSession
from repository.category_repository import CategoryRepository
from repository.color_repository import ColorRepository
from repository.ingredient_repository import IngredientRepository
from schemas.request.category_request import CategoryRequestSchema, CategoryPatchRequestSchema
from schemas.response.category_response import CategoryResponseSchema, CategoriesResponseSchema, DeleteCategoryResponseSchema
from schemas.response.category_response import CategoryIngredientsResponseSchema
from schemas.response.ingredient_response import IngredientForCategoryResponseSchema
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from uuid import UUID


class CategoryService:
    def __init__(self, db: AsyncSession):
        self.category_repository = CategoryRepository(db)
        self.color_repository = ColorRepository(db)
        self.ingredient_repository = IngredientRepository(db)

    async def create_category(self, payload: CategoryRequestSchema) -> CategoryResponseSchema:
        try:
            color = await self.color_repository.get_by_id(color_id=payload.color_id)
            if not color:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Цвет не найден")
            category = await self.category_repository.post(name=payload.name, color_id=payload.color_id)
            return CategoryResponseSchema(
                id=category.id,
                name=category.name,
                color_id=category.color_id
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Категория с таким названием уже существует."
            )

    async def get_all_categories(self) -> CategoriesResponseSchema:
        categories = await self.category_repository.get_all()
        response_categories = []
        for category in categories:
            response_categories.append(
                CategoryResponseSchema(
                    id=category.id,
                    name=category.name,
                    color_id=category.color_id
                )
            )
        return CategoriesResponseSchema(
            categories=response_categories
        )

    async def get_category_ingredients(self, category_id: UUID) -> CategoryIngredientsResponseSchema:
        category, color_hex = await self.category_repository.get_with_color_code_and_ingredients(category_id=category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Категория с id {category_id} не найдена"
            )
        return CategoryIngredientsResponseSchema(
            color=color_hex,
            ingredients=[
                IngredientForCategoryResponseSchema.model_validate(ingredient) for ingredient in category.ingredients
            ]
        )

    async def patch_category(self, category_id: UUID, payload: CategoryPatchRequestSchema) -> CategoryResponseSchema:
        category = await self.category_repository.get_by_id(category_id=category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Категория не найдена")

        if payload.name:
            category.name = payload.name
        if payload.color_id:
            color = await self.color_repository.get_by_id(color_id=payload.color_id)
            if not color:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Цвет не найден")
            category.color_id = payload.color_id

        try:
            updated_category = await self.category_repository.patch(category=category)
            return CategoryResponseSchema(
                id=updated_category.id,
                name=updated_category.name,
                color_id=updated_category.color_id
            )
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Категория с таким названием уже существует"
            )

    async def delete_category(self, category_id: UUID) -> DeleteCategoryResponseSchema:
        row_count = await self.category_repository.delete(category_id=category_id)
        return DeleteCategoryResponseSchema(
            id=category_id,
            row_count=row_count
        )
