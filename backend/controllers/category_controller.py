from fastapi import APIRouter, Depends
from schemas.request.category_request import CreateCategorySchema
from schemas.response.category_response import CategoryResponseSchema
from services.category_service import CategoryService
from dependencies import get_category_service


router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


@router.post("", response_model=CategoryResponseSchema)
async def create_category(
        payload: CreateCategorySchema,
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.create_category(payload=payload)
