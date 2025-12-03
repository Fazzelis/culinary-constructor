from sqlalchemy.ext.asyncio import AsyncSession
from repository.attachment_repository import AttachmentRepository
from fastapi import UploadFile, File, HTTPException, status
import uuid
import os
from schemas.response.attachment_response import AttachmentResponseSchema
from uuid import UUID
import mimetypes
from fastapi.responses import FileResponse


class AttachmentService:
    def __init__(self, db: AsyncSession):
        self.attachment_repository = AttachmentRepository(db)

    async def load_attachment(self, file: UploadFile = File(...)) -> AttachmentResponseSchema:
        filename = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
        file_path = os.path.join("attachments", filename)
        with open(file_path, "wb") as new_file:
            new_file.write(file.file.read())
        attachment = await self.attachment_repository.post(file_path=file_path)
        return AttachmentResponseSchema(
            id=attachment.id,
            file_path=attachment.path
        )

    async def get_attachment(self, attachment_id: UUID):
        attachment = await self.attachment_repository.get_by_id(attachment_id=attachment_id)
        if not attachment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Файл с id {attachment_id} не найден")
        filename = os.path.basename(attachment.path)
        mime_type, _ = mimetypes.guess_type(attachment.path)
        if mime_type is None:
            mime_type = "application/octet-stream"
        return FileResponse(
            path=attachment.path,
            filename=filename,
            media_type=mime_type,
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
