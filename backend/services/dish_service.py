from sqlalchemy.ext.asyncio import AsyncSession
from schemas.request.dish_request import DishRequestSchema
from repository.dish_repository import DishRepository
from repository.recipe_step_repository import RecipeStepRepository
from repository.dish_ingredient_association_repository import DishIngredientRepository
from repository.attachment_repository import AttachmentRepository
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from schemas.response.dish_response import DishResponseSchema
from schemas.internal.ingredient_schema import IngredientSchema
from schemas.internal.recipe_schema import RecipeSchema
from configuration import settings


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
