from sqlalchemy.ext.asyncio import AsyncSession
from schemas.request.dish_request import DishRequestSchema
from repository.dish_repository import DishRepository
from repository.recipe_step_repository import RecipeStepRepository
from repository.dish_ingredient_association_repository import DishIngredientRepository
from repository.attachment_repository import AttachmentRepository
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from schemas.response.dish_response import DishResponseSchema, DishesResponseSchema
from configuration import settings
from uuid import UUID
from schemas.internal.ingredient_schema import IngredientSchema
from schemas.internal.recipe_schema import RecipeSchema
from schemas.internal.dish_schema import DishForCatalogSchema
from schemas.internal.pagination_schema import PaginationSchema


class DishService:
    def __init__(self, db: AsyncSession):
        self.dish_repository = DishRepository(db)
        self.recipe_step_repository = RecipeStepRepository(db)
        self.dish_ingredient_repository = DishIngredientRepository(db)
        self.attachment_repository = AttachmentRepository(db)

    async def create_dish(self, payload: DishRequestSchema) -> DishResponseSchema:
        attachment = await self.attachment_repository.get_by_id(attachment_id=payload.img_id)
        if not attachment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Attachment с id {payload.img_id} не найден"
            )
        icon_url = settings.get_attachment_url + str(attachment.id)
        dish = await self.dish_repository.post(name=payload.name, description=payload.description, img=icon_url)
        try:
            recipe_steps = []
            for recipe_step in payload.recipe_steps:
                recipe_steps.append(
                    RecipeSchema.model_validate(
                        await self.recipe_step_repository.post(
                            step_number=recipe_step.step_number,
                            description=recipe_step.description,
                            dish_id=dish.id
                        )
                    )
                )

            dish_ingredient_association = []
            for ingredient_id, count in payload.ingredients.items():
                association = await self.dish_ingredient_repository.post(
                    dish_id=dish.id,
                    ingredient_id=ingredient_id,
                    count=count
                )
                dish_ingredient_association.append(IngredientSchema(
                    id=association.ingredient_id,
                    name=association.ingredient.name,
                    count=association.count
                ))
            return DishResponseSchema(
                id=dish.id,
                name=dish.name,
                description=dish.description,
                img=dish.img,
                ingredients=dish_ingredient_association,
                recipe_steps=recipe_steps
            )
        except IntegrityError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e.orig}")

    async def get_dish(self, dish_id: UUID) -> DishResponseSchema:
        dish = await self.dish_repository.get(dish_id=dish_id)
        if not dish:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Блюдо с id {dish_id} не найдено"
            )
        ingredients = []
        for ingredient_association in dish.ingredient_associations:
            ingredients.append(
                IngredientSchema(
                    id=ingredient_association.ingredient.id,
                    name=ingredient_association.ingredient.name,
                    count=ingredient_association.count
                )
            )

        recipe_steps = []
        for recipe_step in dish.recipe_steps:
            recipe_steps.append(
                RecipeSchema(
                    id=recipe_step.id,
                    step_number=recipe_step.step_number,
                    description=recipe_step.description
                )
            )

        return DishResponseSchema(
            id=dish.id,
            name=dish.name,
            description=dish.description,
            img=dish.img,
            ingredients=ingredients,
            recipe_steps=recipe_steps
        )

    async def get_all_dishes(self, page: int, page_size: int) -> DishesResponseSchema:
        dishes, total_count = await self.dish_repository.get_all(page=page, page_size=page_size)
        dishes_response = []
        for dish in dishes:
            dishes_response.append(
                DishForCatalogSchema(
                    id=dish.id,
                    name=dish.name,
                    description=dish.description,
                    img=dish.img
                )
            )

        return DishesResponseSchema(
            pagination=PaginationSchema(
                page=page,
                page_size=page_size,
                total_count=total_count,
                total_pages=(total_count + page_size - 1) // page_size
            ),
            dishes=dishes_response
        )
