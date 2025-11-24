from sqlalchemy.ext.asyncio import AsyncSession
from repository.recipe_step_repository import RecipeStepRepository
from schemas.request.recipe_step_request import RecipeStepRequest


class RecipeStepService:
    def __init__(self, db: AsyncSession):
        self.recipe_step_repository = RecipeStepRepository(db)

    async def create_recipe_step(self, payload: RecipeStepRequest):
        pass
