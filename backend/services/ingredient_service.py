from sqlalchemy.ext.asyncio import AsyncSession
from repository.ingredient_repository import IngredientRepository
from repository.category_repository import CategoryRepository
from schemas.request.ingredient_request import IngredientRequestSchema
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from schemas.response.ingredient_response import IngredientResponseSchema


class IngredientService:
    def __init__(self, db: AsyncSession):
        self.ingredient_repository = IngredientRepository(db)
        self.category_repository = CategoryRepository(db)

    async def create_ingredient(self, payload: IngredientRequestSchema) -> IngredientResponseSchema:
        try:
            category = await self.category_repository.get_by_id(category_id=payload.category_id)
            if not category:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Категория с id {payload.category_id} не найдена"
                )
            ingredient = await self.ingredient_repository.post(name=payload.name, category_id=payload.category_id)
            return IngredientResponseSchema(
                id=ingredient.id,
                name=ingredient.name,
                category_id=ingredient.category_id
            )
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ингредиент с таким названием уже существует"
            )
