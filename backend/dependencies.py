from services.color_service import ColorService
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_color_service(db: AsyncSession = Depends(get_db)):
    return ColorService(db)
