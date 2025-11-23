from services.color_service import ColorService
from services.category_service import CategoryService
from services.ingredient_service import IngredientService
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_color_service(db: AsyncSession = Depends(get_db)):
    return ColorService(db)


async def get_category_service(db: AsyncSession = Depends(get_db)):
    return CategoryService(db)


async def get_ingredient_service(db: AsyncSession = Depends(get_db)):
    return IngredientService(db)
