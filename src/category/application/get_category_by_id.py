from src.category.domain.repository import CategoryRepositoryInterface
from src.category.infrastructure.model import Category


class GetCategoryById:

    def __init__(
        self,
        repository: CategoryRepositoryInterface,
    ):
        self.repository = repository

    def execute(
        self,
        category_id: int,
    ) -> Category | None:

        return self.repository.get_by_id(category_id)