from fastapi import APIRouter
from controllers.color_controller import router as color_router


router = APIRouter()
router.include_router(color_router)
