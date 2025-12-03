from database.database import Base
from sqlalchemy import Column, func, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String, unique=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("category.id"))

    category = relationship("Category", back_populates="ingredients")
    dish_associations = relationship("DishIngredientAssociation", back_populates="ingredient")
