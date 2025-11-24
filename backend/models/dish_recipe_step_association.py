from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.orm import relationship


class DishRecipeStepAssociation(Base):
    __tablename__ = "dish_recipe_step_association"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())

    dish_id = Column(UUID(as_uuid=True), ForeignKey("dish.id"))
    recipe_step_id = Column(UUID(as_uuid=True), ForeignKey("recipe_step.id"))

    dish = relationship("Dish", back_populates="recipe_step_associations")
    recipe_step = relationship("RecipeStep", back_populates="dish_associations")
