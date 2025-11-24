from sqlalchemy.ext.asyncio import AsyncSession
from models.ingredient import Ingredient
from sqlalchemy.exc import IntegrityError
from uuid import UUID


class IngredientRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, name: str, category_id: UUID):
        try:
            ingredient = Ingredient(
                name=name,
                category_id=category_id
            )
            self.db.add(ingredient)
            await self.db.commit()
            await self.db.refresh(ingredient)
            return ingredient
        except IntegrityError as e:
            raise e
