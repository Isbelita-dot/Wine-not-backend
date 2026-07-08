from src.wine.domain.repository import WineRepositoryInterface
from src.wine.infrastructure.model import Wine
from src.wine.infrastructure.schema import WineCreate


class CreateWine:

    def init(self, repository: WineRepositoryInterface):
        self.repository = repository

    def execute(self, wine: WineCreate) -> Wine:
        return self.repository.create(wine)