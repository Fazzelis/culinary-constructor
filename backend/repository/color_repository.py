from sqlalchemy.ext.asyncio import AsyncSession
from models.color import Color
from sqlalchemy.exc import IntegrityError
from uuid import UUID
from sqlalchemy import select


class ColorRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, name: str, hex_code: str) -> Color:
        color = Color(
            name=name,
            hex_code=hex_code
        )
        self.db.add(color)
        try:
            await self.db.commit()
            await self.db.refresh(color)
            return color
        except IntegrityError as e:
            await self.db.rollback()
            raise e

    async def get_by_id(self, color_id: UUID) -> Color | None:
        result = await self.db.execute(select(Color).where(Color.id == color_id))
        color = result.scalar_one_or_none()
        return color

    async def put(self, name: str, hex_code: str, color: Color) -> Color:
        color.name = name
        color.hex_code = hex_code
        self.db.add(color)
        try:
            await self.db.commit()
            await self.db.refresh(color)
            return color
        except IntegrityError as e:
            await self.db.rollback()
            raise e
