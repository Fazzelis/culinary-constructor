from database.database import Base
from sqlalchemy import Column, func, String
from sqlalchemy.dialects.postgresql import UUID


class Attachment(Base):
    __tablename__ = "attachment"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    path = Column(String, unique=True)
