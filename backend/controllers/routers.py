from fastapi import APIRouter
from controllers.color_controller import router as color_router
from controllers.category_controller import router as category_router
from controllers.ingredient_controller import router as ingredient_router
from controllers.recipe_step_controller import router as recipe_step_router
from controllers.dish_controller import router as dish_router


router = APIRouter()
router.include_router(color_router)
router.include_router(category_router)
router.include_router(ingredient_router)
router.include_router(recipe_step_router)
router.include_router(dish_router)
