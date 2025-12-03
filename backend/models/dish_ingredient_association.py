from database.database import Base
from sqlalchemy import Column, func, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class DishIngredientAssociation(Base):
    __tablename__ = "dish_ingredient_association"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    count = Column(String)

    dish_id = Column(UUID(as_uuid=True), ForeignKey("dish.id"))
    ingredient_id = Column(UUID(as_uuid=True), ForeignKey("ingredient.id"))

    dish = relationship("Dish", back_populates="ingredient_associations")
    ingredient = relationship("Ingredient", back_populates="dish_associations")
