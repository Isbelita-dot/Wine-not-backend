from src.category.domain.repository import CategoryRepositoryInterface
from src.category.infrastructure.model import Category
from src.category.infrastructure.schema import CategoryUpdate


class UpdateCategory:

    def __init__(
        self,
        repository: CategoryRepositoryInterface,
    ):
        self.repository = repository

    def execute(
        self,
        category_id: int,
        category: CategoryUpdate,
    ) -> Category | None:

        return self.repository.update(
            category_id,
            category,
        )