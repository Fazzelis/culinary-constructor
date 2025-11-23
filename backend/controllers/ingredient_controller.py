from fastapi import APIRouter, Depends
from schemas.request.ingredient_request import IngredientRequestSchema
from dependencies import get_ingredient_service
from services.ingredient_service import IngredientService
from schemas.response.ingredient_response import IngredientResponseSchema


router = APIRouter(
    prefix="/ingredient",
    tags=["Ingredient"]
)


@router.post("", response_model=IngredientResponseSchema)
async def create_ingredient(
        payload: IngredientRequestSchema,
        ingredient_service: IngredientService = Depends(get_ingredient_service)
):
    return await ingredient_service.create_ingredient(payload=payload)
