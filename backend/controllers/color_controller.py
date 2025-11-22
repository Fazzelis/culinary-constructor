from fastapi import APIRouter, Depends
from schemas.request.color_request import CreateColorSchema
from services.color_service import ColorService
from dependencies import get_color_service
from schemas.response.color_response import ColorResponseSchema, DeleteColorResponseSchema
from uuid import UUID


router = APIRouter(
    prefix="/color",
    tags=["Color"]
)


@router.post("", response_model=ColorResponseSchema)
async def create_color(
        payload: CreateColorSchema,
        color_service: ColorService = Depends(get_color_service)
):
    return await color_service.create_color(payload=payload)


@router.get("", response_model=ColorResponseSchema)
async def get_color_by_id(
        color_id: UUID,
        color_service: ColorService = Depends(get_color_service)
):
    return await color_service.get_color_by_id(color_id=color_id)


@router.put("", response_model=ColorResponseSchema)
async def update_color(
        color_id: UUID,
        payload: CreateColorSchema,
        color_service: ColorService = Depends(get_color_service)
):
    return await color_service.update_color(color_id=color_id, payload=payload)


@router.delete("", response_model=DeleteColorResponseSchema)
async def delete_color(
        color_id: UUID,
        color_service: ColorService = Depends(get_color_service)
):
    return await color_service.delete_color(color_id=color_id)
