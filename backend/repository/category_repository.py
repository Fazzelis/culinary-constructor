from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from models.category import Category


class CategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, name: str, color_id: UUID) -> Category:
        try:
            category = Category(
                name=name,
                color_id=color_id
            )
            self.db.add(category)
            await self.db.commit()
            await self.db.refresh(category)
            return category
        except IntegrityError as e:
            raise e
