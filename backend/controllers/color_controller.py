from fastapi import APIRouter, Depends
from schemas.request.color_request import CreateColorSchema
from services.color_service import ColorService
from dependencies import get_color_service
from schemas.response.color_response import ColorResponseSchema


router = APIRouter(
    prefix="/color",
    tags=["Color"]
)


@router.post("/create", response_model=ColorResponseSchema)
async def create_color(
        payload: CreateColorSchema,
        color_service: ColorService = Depends(get_color_service)
):
    return await color_service.create_color(payload=payload)
