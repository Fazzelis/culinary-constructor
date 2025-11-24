from sqlalchemy.ext.asyncio import AsyncSession
from schemas.request.dish_request import DishRequestSchema
from repository.dish_repository import DishRepository
from repository.recipe_step_repository import RecipeStepRepository
from repository.dish_ingredient_association_repository import DishIngredientRepository
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from schemas.response.dish_response import DishResponseSchema
from schemas.internal.ingredient_schema import IngredientSchema
from schemas.internal.recipe_schema import RecipeSchema


class DishService:
    def __init__(self, db: AsyncSession):
        self.dish_repository = DishRepository(db)
        self.recipe_step_repository = RecipeStepRepository(db)
        self.dish_ingredient_repository = DishIngredientRepository(db)

    async def create_dish(self, payload: DishRequestSchema) -> DishResponseSchema:
        dish = await self.dish_repository.post(name=payload.name)

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
                ingredients=dish_ingredient_association,
                recipe_steps=recipe_steps
            )
        except IntegrityError as e:
            await self.dish_repository.delete(dish_id=dish.id)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.orig)
