from sqlalchemy.ext.asyncio import AsyncSession
from models.attachment import Attachment
from uuid import UUID
from sqlalchemy import select


class AttachmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(self, file_path: str) -> Attachment:
        attachment = Attachment(path=file_path)
        self.db.add(attachment)
        await self.db.commit()
        await self.db.refresh(attachment)
        return attachment

    async def get_by_id(self, attachment_id: UUID) -> Attachment | None:
        result = await self.db.execute(select(Attachment).where(Attachment.id == attachment_id))
        attachment = result.scalar_one_or_none()
        return attachment
