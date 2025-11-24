from sqlalchemy.ext.asyncio import AsyncSession


class RecipeStepRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
