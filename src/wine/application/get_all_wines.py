from src.wine.domain.repository import WineRepositoryInterface
from src.wine.infrastructure.model import Wine


class GetAllWines:

    def __init__(self, repository: WineRepositoryInterface):
        self.repository = repository

    def execute(self) -> list[Wine]:
        return self.repository.get_all()