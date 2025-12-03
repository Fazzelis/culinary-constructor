from fastapi import APIRouter, Depends, UploadFile, File
from dependencies import get_attachment_service
from services.attachment_service import AttachmentService
from schemas.response.attachment_response import AttachmentResponseSchema
from uuid import UUID
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/attachment",
    tags=["Attachment"]
)


@router.post("/load-file", response_model=AttachmentResponseSchema)
async def load_def(
        file: UploadFile = File(...),
        attachment_service: AttachmentService = Depends(get_attachment_service)
):
    return await attachment_service.load_attachment(file=file)


@router.get("", response_class=FileResponse)
async def get_attachment(
        attachment_id: UUID,
        attachments_service: AttachmentService = Depends(get_attachment_service)
):
    return await attachments_service.get_attachment(attachment_id=attachment_id)
