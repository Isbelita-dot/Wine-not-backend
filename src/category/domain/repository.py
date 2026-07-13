from abc import ABC, abstractmethod

from src.category.infrastructure.model import Category
from src.category.infrastructure.schema import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryRepositoryInterface(ABC):

    @abstractmethod
    def create(
        self,
        category: CategoryCreate,
    ) -> Category:
        pass

    @abstractmethod
    def get_all(self) -> list[Category]:
        pass

    @abstractmethod
    def get_by_id(
        self,
        category_id: int,
    ) -> Category | None:
        pass

    @abstractmethod
    def update(
        self,
        category_id: int,
        category: CategoryUpdate,
    ) -> Category | None:
        pass

    @abstractmethod
    def delete(
        self,
        category_id: int,
    ) -> bool:
        pass