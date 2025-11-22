from sqlalchemy.ext.asyncio import AsyncSession
from models.color import Color
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


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
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Имя или код цвета уже существуют. {e.orig}"
            )
