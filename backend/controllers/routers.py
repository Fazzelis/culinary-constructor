from fastapi import APIRouter
from controllers.color_controller import router as color_router
from controllers.category_controller import router as category_router


router = APIRouter()
router.include_router(color_router)
router.include_router(category_router)
