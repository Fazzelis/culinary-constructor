from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class CategoryRequestSchema(BaseModel):
    name: str
    color_id: UUID


class CategoryPatchRequestSchema(BaseModel):
    name: Optional[str] = None
    color_id: Optional[UUID] = None
