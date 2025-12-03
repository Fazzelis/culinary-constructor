from pydantic import BaseModel, Field


class CreateColorSchema(BaseModel):
    name: str
    hex_code: str = Field(..., min_length=7, max_length=7)
