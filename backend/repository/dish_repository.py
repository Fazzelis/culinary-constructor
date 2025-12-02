from sqlalchemy.ext.asyncio import AsyncSession
from models.dish import Dish
from models.dish_ingredient_association import DishIngredientAssociation
from sqlalchemy import select, delete, func
from sqlalchemy.orm import selectinload
from uuid import UUID


class DishRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def post(
            self,
            name: str,
            description: str,
            img: str,
            protein: int = None,
            fats: int = None,
            carbs: int = None,
            calories: int = None
    ) -> Dish:
        dish = Dish(
            name=name,
            description=description,
            img=img,
            protein=protein,
            fats=fats,
            carbs=carbs,
            calories=calories
        )
        self.db.add(dish)
        await self.db.commit()
        await self.db.refresh(dish)
        return dish

    async def get(self, dish_id: UUID) -> Dish | None:
        result = await self.db.execute(
            select(Dish)
            .options(
                selectinload(Dish.recipe_steps),
                selectinload(Dish.ingredient_associations)
                .selectinload(DishIngredientAssociation.ingredient)
            )
            .where(Dish.id == dish_id)
        )
        dish = result.scalar_one_or_none()
        return dish

    async def get_all(self, page: int, page_size: int):
        offset = (page - 1) * page_size
        result = await self.db.execute(
            select(Dish)
            .offset(offset)
            .limit(page_size)
            .options(
                selectinload(Dish.ingredient_associations)
            )
        )
        dishes = result.scalars().all()
        count_result = await self.db.execute(select(func.count(Dish.id)))
        total_count = count_result.scalar_one()
        return dishes, total_count

    async def get_by_ingredient_ids(self, ingredient_ids: list[UUID], page: int, page_size: int):
        ingredients_count = len(ingredient_ids)
        offset = (page - 1) * page_size
        result = await self.db.execute(
            select(Dish)
            .join(Dish.ingredient_associations)
            .where(DishIngredientAssociation.ingredient_id.in_(ingredient_ids))
            .group_by(Dish.id)
            .having(func.count(DishIngredientAssociation.ingredient_id) == ingredients_count)
            .order_by(func.count(DishIngredientAssociation.ingredient_id).asc())
            .offset(offset)
            .limit(page_size)
            .options(
                selectinload(Dish.recipe_steps),
                selectinload(Dish.ingredient_associations)
                .selectinload(DishIngredientAssociation.ingredient)
            )
        )

        dishes = result.scalars().all()

        matching_dishes_subquery = (
            select(Dish.id)
            .join(Dish.ingredient_associations)
            .where(DishIngredientAssociation.ingredient_id.in_(ingredient_ids))
            .group_by(Dish.id)
            .having(func.count(DishIngredientAssociation.ingredient_id) == ingredients_count)
        ).subquery()

        count_result = await self.db.execute(
            select(func.count()).select_from(matching_dishes_subquery)
        )
        total_count = count_result.scalar_one()

        return dishes, total_count

    async def delete(self, dish_id: UUID):
        result = await self.db.execute(delete(Dish).where(Dish.id == dish_id))
        await self.db.commit()
        return result.rowcount
