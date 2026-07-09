from src.category.domain.repository import CategoryRepositoryInterface


class DeleteCategory:

    def __init__(
        self,
        repository: CategoryRepositoryInterface,
    ):
        self.repository = repository

    def execute(
        self,
        category_id: int,
    ) -> bool:

        return self.repository.delete(category_id)