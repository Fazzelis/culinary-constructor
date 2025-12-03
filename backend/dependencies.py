from services.color_service import ColorService
from services.category_service import CategoryService
from services.ingredient_service import IngredientService
from services.recipe_step_service import RecipeStepService
from services.attachment_service import AttachmentService
from services.dish_service import DishService
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_color_service(db: AsyncSession = Depends(get_db)):
    return ColorService(db)


async def get_category_service(db: AsyncSession = Depends(get_db)):
    return CategoryService(db)


async def get_ingredient_service(db: AsyncSession = Depends(get_db)):
    return IngredientService(db)


async def get_recipe_step_service(db: AsyncSession = Depends(get_db)):
    return RecipeStepService(db)


async def get_dish_service(db: AsyncSession = Depends(get_db)):
    return DishService(db)


async def get_attachment_service(db: AsyncSession = Depends(get_db)):
    return AttachmentService(db)
