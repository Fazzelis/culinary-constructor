from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from models.recipe_step import RecipeStep
from sqlalchemy.exc import IntegrityError


class RecipeStepRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, step_number: int, description: str, dish_id: UUID) -> RecipeStep:
        try:
            recipe_step = RecipeStep(
                step_number=step_number,
                description=description,
                dish_id=dish_id
            )
            self.db.add(recipe_step)
            await self.db.commit()
            await self.db.refresh(recipe_step)
            return recipe_step
        except IntegrityError as e:
            raise e
