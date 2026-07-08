from src.wine.domain.repository import WineRepositoryInterface
from src.wine.infrastructure.model import Wine
from src.wine.infrastructure.schema import WineUpdate


class UpdateWine:

    def init(self, repository: WineRepositoryInterface):
        self.repository = repository

    def execute(
        self,
        wine_id: int,
        wine: WineUpdate,
    ) -> Wine | None:
        return self.repository.update(wine_id, wine)