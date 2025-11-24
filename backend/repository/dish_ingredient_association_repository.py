from sqlalchemy.ext.asyncio import AsyncSession
from models.dish_ingredient_association import DishIngredientAssociation
from uuid import UUID
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from models.ingredient import Ingredient


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
            await self.db.rollback()
            raise e

    # async def get_by_dish_id(self, dish_id: UUID):
    #     result = await self.db.execute(
    #         select(DishIngredientAssociation, Ingredient.name)
    #         .join(Ingredient, DishIngredientAssociation.ingredient_id == Ingredient.id)
    #         .where(DishIngredientAssociation.dish_id == dish_id)
    #     )
    #
    #     response = result
