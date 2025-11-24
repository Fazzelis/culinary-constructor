from sqlalchemy.ext.asyncio import AsyncSession
from models.dish_ingredient_association import DishIngredientAssociation
from uuid import UUID
from sqlalchemy.exc import IntegrityError


class DishIngredientRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, dish_id: UUID, ingredient_id: UUID, count: str) -> DishIngredientAssociation:
        try:
            association = DishIngredientAssociation(
                count=count,
                dish_id=dish_id,
                ingredient_id=ingredient_id
            )
            self.db.add(association)
            await self.db.commit()
            await self.db.refresh(association, ["ingredient"])
            return association
        except IntegrityError as e:
            raise e
