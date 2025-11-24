from pydantic import BaseModel
from uuid import UUID


class AttachmentResponseSchema(BaseModel):
    id: UUID
    file_path: str
