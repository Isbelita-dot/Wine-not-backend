from src.category.domain.repository import CategoryRepositoryInterface
from src.category.infrastructure.model import Category
from src.category.infrastructure.schema import CategoryCreate


class CreateCategory:

    def __init__(
        self,
        repository: CategoryRepositoryInterface,
    ):
        self.repository = repository

    def execute(
        self,
        category: CategoryCreate,
    ) -> Category:

        return self.repository.create(category)