from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, String
from sqlalchemy.orm import relationship


class Color(Base):
    __tablename__ = "color"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String, unique=True)
    hex_code = Column(String, unique=True)

    categories = relationship("Category", back_populates="color")
