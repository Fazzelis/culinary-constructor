from database.database import Base
from sqlalchemy import Column, Text, func, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class RecipeStep(Base):
    __tablename__ = "recipe_step"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    step_number = Column(Integer)
    description = Column(Text)
    dish_id = Column(UUID(as_uuid=True), ForeignKey("dish.id"))

    dish = relationship("Dish", back_populates="recipe_steps")
