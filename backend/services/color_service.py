from sqlalchemy.ext.asyncio import AsyncSession
from repository.color_repository import ColorRepository
from schemas.request.color_request import CreateColorSchema
from schemas.response.color_response import ColorResponseSchema


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
