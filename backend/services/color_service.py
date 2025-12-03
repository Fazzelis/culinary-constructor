from sqlalchemy.ext.asyncio import AsyncSession
from repository.color_repository import ColorRepository
from schemas.request.color_request import CreateColorSchema
from schemas.response.color_response import ColorResponseSchema, DeleteColorResponseSchema
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


class ColorService:
    def __init__(self, db: AsyncSession):
        self.color_repository = ColorRepository(db)

    async def create_color(self, payload: CreateColorSchema) -> ColorResponseSchema:
        try:
            created_color = await self.color_repository.post(name=payload.name, hex_code=payload.hex_code)
            return ColorResponseSchema(
                id=created_color.id,
                name=created_color.name,
                hex_code=created_color.hex_code
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Имя или код цвета уже существуют. {e.orig}"
            )

    async def get_color_by_id(self, color_id: UUID) -> ColorResponseSchema:
        color = await self.color_repository.get_by_id(color_id=color_id)
        if not color:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Цвет с id = {color_id} не найден")
        return ColorResponseSchema(
            id=color.id,
            name=color.name,
            hex_code=color.hex_code
        )

    async def update_color(
            self,
            color_id: UUID,
            payload: CreateColorSchema
    ) -> ColorResponseSchema:
        try:
            old_color = await self.color_repository.get_by_id(color_id=color_id)
            if not old_color:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Цвет с id = {color_id} не найден")
            new_color = await self.color_repository.put(name=payload.name, hex_code=payload.hex_code, color=old_color)
            return ColorResponseSchema(
                id=new_color.id,
                name=new_color.name,
                hex_code=new_color.hex_code
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Имя или код цвета уже существуют. {e.orig}"
            )

    async def delete_color(self, color_id: UUID) -> DeleteColorResponseSchema:
        row_count = await self.color_repository.delete(color_id=color_id)
        return DeleteColorResponseSchema(
            id=color_id,
            rowcount=row_count
        )
