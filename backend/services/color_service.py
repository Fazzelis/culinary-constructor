from sqlalchemy.ext.asyncio import AsyncSession
from repository.color_repository import ColorRepository
from schemas.request.color_request import CreateColorSchema
from schemas.response.color_response import ColorResponseSchema
from uuid import UUID
from fastapi import HTTPException, status


class ColorService:
    def __init__(self, db: AsyncSession):
        self.repo = ColorRepository(db)

    async def create_color(self, payload: CreateColorSchema):
        created_color = await self.repo.post(name=payload.name, hex_code=payload.hex_code)
        return ColorResponseSchema(
            id=created_color.id,
            name=created_color.name,
            hex_code=created_color.hex_code
        )

    async def get_color_by_id(self, color_id: UUID):
        color = await self.repo.get_by_id(color_id=color_id)
        if not color:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Цвет с id = {color_id} не найден")
        return ColorResponseSchema(
            id=color.id,
            name=color.name,
            hex_code=color.hex_code
        )
