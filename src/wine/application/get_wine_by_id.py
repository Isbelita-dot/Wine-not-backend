from src.wine.domain.repository import WineRepositoryInterface
from src.wine.infrastructure.model import Wine


class GetWineById:

    def init(self, repository: WineRepositoryInterface):
        self.repository = repository

    def execute(self, wine_id: int) -> Wine | None:
        return self.repository.get_by_id(wine_id)