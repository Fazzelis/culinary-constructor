from pydantic import BaseModel
from uuid import UUID


class CreateCategorySchema(BaseModel):
    name: str
    color_id: UUID
