from abc import ABC, abstractmethod

from src.wine.infrastructure.model import Wine
from src.wine.infrastructure.schema import WineCreate, WineUpdate


class WineRepositoryInterface(ABC):
    @abstractmethod
    def create(self, wine: WineCreate) -> Wine:
        pass

    @abstractmethod
    def get_all(self) -> list[Wine]:
        pass

    @abstractmethod
    def get_by_id(self, wine_id: int) -> Wine | None:
        pass

    @abstractmethod
    def update(
        self,
        wine_id: int,
        wine: WineUpdate,
    ) -> Wine | None:
        pass

    @abstractmethod
    def delete(self, wine_id: int) -> bool:
        pass