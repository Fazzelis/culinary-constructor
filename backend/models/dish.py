from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, String, Integer
from sqlalchemy.orm import relationship
from models.recipe_step import RecipeStep


class Dish(Base):
    __tablename__ = "dish"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String)
    description = Column(String)
    img = Column(String)
    protein = Column(Integer)
    fats = Column(Integer)
    carbs = Column(Integer)
    calories = Column(Integer)

    recipe_steps = relationship("RecipeStep", back_populates="dish", order_by=RecipeStep.step_number)
    ingredient_associations = relationship("DishIngredientAssociation", back_populates="dish")
