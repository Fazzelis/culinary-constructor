from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from models.category import Category
from models.color import Color
from typing import Sequence


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

    async def get_all(self) -> Sequence[Category] | None:
        result = await self.db.execute(select(Category))
        categories = result.scalars().all()
        return categories

    async def get_by_id(self, category_id: UUID) -> Category | None:
        result = await self.db.execute(select(Category).where(Category.id == category_id))
        category = result.scalar_one_or_none()
        return category

    async def get_with_color_code_and_ingredients(self, category_id: UUID):
        result = await self.db.execute(
            select(Category, Color.hex_code)
            .join(Color, Category.color_id == Color.id)
            .options(selectinload(Category.ingredients))
            .where(Category.id == category_id)
        )

        response = result.first()
        if response:
            category, color_hex = response
            return category, color_hex
        return None, None

    async def patch(self, category: Category) -> Category:
        try:
            self.db.add(category)
            await self.db.commit()
            await self.db.refresh(category)
            return category
        except IntegrityError as e:
            raise e

    async def delete(self, category_id: UUID) -> int:
        result = await self.db.execute(delete(Category).where(Category.id == category_id))
        await self.db.commit()
        return result.rowcount
