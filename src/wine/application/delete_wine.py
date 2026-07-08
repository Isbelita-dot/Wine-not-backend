from src.wine.domain.repository import WineRepositoryInterface


class DeleteWine:

    def __init__(self, repository: WineRepositoryInterface):
        self.repository = repository

    def execute(self, wine_id: int) -> bool:
        return self.repository.delete(wine_id)