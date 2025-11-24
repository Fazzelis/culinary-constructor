from sqlalchemy.ext.asyncio import AsyncSession
from models.dish import Dish
from sqlalchemy import delete
from uuid import UUID


class DishRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, name: str, description: str) -> Dish:
        dish = Dish(name=name, description=description)
        self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(dish)
        return dish

    async def delete(self, dish_id: UUID):
        result = await self.db.execute(delete(Dish).where(Dish.id == dish_id))
        await self.db.commit()
        return result.rowcount
