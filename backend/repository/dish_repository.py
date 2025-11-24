from sqlalchemy.ext.asyncio import AsyncSession
from models.dish import Dish
from models.dish_ingredient_association import DishIngredientAssociation
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from uuid import UUID


class DishRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, name: str, description: str, img: str) -> Dish:
        dish = Dish(name=name, description=description, img=img)
        self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(dish)
        return dish

    async def get(self, dish_id: UUID) -> Dish | None:
        result = await self.db.execute(
            select(Dish)
            .options(
                selectinload(Dish.recipe_steps),
                selectinload(Dish.ingredient_associations)
                .selectinload(DishIngredientAssociation.ingredient)
            )
            .where(Dish.id == dish_id)
        )
        dish = result.scalar_one_or_none()
        return dish

    async def delete(self, dish_id: UUID):
        result = await self.db.execute(delete(Dish).where(Dish.id == dish_id))
        await self.db.commit()
        return result.rowcount
