from sqlalchemy.orm import Session

from src.category.domain.repository import CategoryRepositoryInterface
from src.category.infrastructure.model import Category
from src.category.infrastructure.schema import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryRepository(CategoryRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        category: CategoryCreate,
    ) -> Category:

        db_category = Category(
            name=category.name,
            description=category.description,
        )

        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)

        return db_category

    def get_all(self) -> list[Category]:
        return self.db.query(Category).all()

    def get_by_id(
        self,
        category_id: int,
    ) -> Category | None:

        return (
            self.db.query(Category)
            .filter(Category.id == category_id)
            .first()
        )

    def update(
        self,
        category_id: int,
        category: CategoryUpdate,
    ) -> Category | None:

        db_category = self.get_by_id(category_id)

        if db_category is None:
            return None

        db_category.name = category.name
        db_category.description = category.description

        self.db.commit()
        self.db.refresh(db_category)

        return db_category

    def delete(
        self,
        category_id: int,
    ) -> bool:

        db_category = self.get_by_id(category_id)

        if db_category is None:
            return False

        self.db.delete(db_category)
        self.db.commit()

        return True