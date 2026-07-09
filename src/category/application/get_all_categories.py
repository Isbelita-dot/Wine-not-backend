from src.category.domain.repository import CategoryRepositoryInterface
from src.category.infrastructure.model import Category


class GetAllCategories:

    def __init__(
        self,
        repository: CategoryRepositoryInterface,
    ):
        self.repository = repository

    def execute(self) -> list[Category]:
        return self.repository.get_all()