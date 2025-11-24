from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, String
from sqlalchemy.orm import relationship


class Dish(Base):
    __tablename__ = "dish"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    name = Column(String)

    recipe_step_associations = relationship("DishRecipeStepAssociation", back_populates='dish')
