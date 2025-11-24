from fastapi import APIRouter, Depends
from schemas.request.dish_request import DishRequestSchema
from dependencies import get_dish_service
from services.dish_service import DishService


router = APIRouter(
    prefix="/dish",
    tags=["Dish"]
)


@router.post("")
async def create_dish(
        payload: DishRequestSchema,
        dish_service: DishService = Depends(get_dish_service)
):
    return await dish_service.create_dish(payload=payload)
