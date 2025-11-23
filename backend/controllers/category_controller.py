from fastapi import APIRouter, Depends
from schemas.request.category_request import CategoryRequestSchema, CategoryPatchRequestSchema
from schemas.response.category_response import CategoryResponseSchema, CategoriesResponseSchema, DeleteCategoryResponseSchema
from services.category_service import CategoryService
from dependencies import get_category_service
from uuid import UUID


router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


@router.post("", response_model=CategoryResponseSchema)
async def create_category(
        payload: CategoryRequestSchema,
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.create_category(payload=payload)


@router.get("", response_model=CategoriesResponseSchema)
async def get_all_categories(
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.get_all_categories()


@router.get("/ingredients")
async def get_category_ingredients(
        category_id: UUID,
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.get_category_ingredients(category_id=category_id)


@router.patch("", response_model=CategoryResponseSchema)
async def patch_category(
        category_id: UUID,
        payload: CategoryPatchRequestSchema,
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.patch_category(category_id=category_id, payload=payload)


@router.delete("", response_model=DeleteCategoryResponseSchema)
async def delete_category(
        category_id: UUID,
        category_service: CategoryService = Depends(get_category_service)
):
    return await category_service.delete_category(category_id=category_id)
