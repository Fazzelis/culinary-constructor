from fastapi import APIRouter, Depends, Query
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
        page: int = Query(1, ge=1, description="Номер страницы"),
        page_size: int = Query(5, ge=1, le=100, description="Количество элементов на одной странице"),
        dish_service: DishService = Depends(get_dish_service)
):
    return await dish_service.get_all_dishes(page=page, page_size=page_size)
