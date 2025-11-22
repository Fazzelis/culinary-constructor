from pydantic import BaseModel
from uuid import UUID


class ColorResponseSchema(BaseModel):
    id: UUID
    name: str
    hex_code: str


class DeleteColorResponseSchema(BaseModel):
    id: UUID
    rowcount: int
