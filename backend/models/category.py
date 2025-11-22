from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String, unique=True)

    color_id = Column(UUID(as_uuid=True), ForeignKey("color.id"))
    color = relationship("Color", back_populates="categories")

    ingredients = relationship("Ingredient", back_populates="category")
