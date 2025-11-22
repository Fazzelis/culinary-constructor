from fastapi import APIRouter, Depends
from schemas.request.category_request import CreateCategorySchema
from schemas.response.category_response import CategoryResponseSchema, CategoriesResponseSchema
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


@router.get("", response_model=CategoriesResponseSchema)
async def get_all_categories(
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.get_all_categories()
