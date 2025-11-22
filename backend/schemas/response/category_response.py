from pydantic import BaseModel
from uuid import UUID


class CategoryResponseSchema(BaseModel):
    id: UUID
    name: str
    color_id: UUID
