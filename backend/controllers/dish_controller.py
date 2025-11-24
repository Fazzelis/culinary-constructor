from fastapi import APIRouter, Depends
from schemas.request.dish_request import DishRequestSchema
from dependencies import get_dish_service
from services.dish_service import DishService
from schemas.response.dish_response import DishResponseSchema
from uuid import UUID


router = APIRouter(
    prefix="/dish",
    tags=["Dish"]
)


@router.post("", response_model=DishResponseSchema)
async def create_dish(
        payload: DishRequestSchema,
        dish_service: DishService = Depends(get_dish_service)
):
    return await dish_service.create_dish(payload=payload)


@router.get("", response_model=DishResponseSchema)
async def get_dish(
        dish_id: UUID,
        dish_service: DishService = Depends(get_dish_service)
):
    return await dish_service.get_dish(dish_id=dish_id)


@router.get("/all")
async def get_all_dishes(
        dish_service: DishService = Depends(get_dish_service)
):
    return await dish_service.get_all_dishes()
