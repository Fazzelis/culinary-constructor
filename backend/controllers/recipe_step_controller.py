from fastapi import APIRouter, Depends
from schemas.request.recipe_step_request import RecipeStepRequest
from dependencies import get_recipe_step_service
from services.recipe_step_service import RecipeStepService


router = APIRouter(
    prefix="/recipe-step",
    tags=["RecipeStep"]
)


@router.post("")
async def create_recipe_step(
        payload: RecipeStepRequest,
        recipe_step_service: RecipeStepService = Depends(get_recipe_step_service)
):
    return recipe_step_service.create_recipe_step(payload=payload)
