from sqlalchemy.orm import Session

from src.shared.infrastructure.database import SessionLocal
from src.wine.domain.repository import WineRepositoryInterface
from src.wine.infrastructure.model import Wine
from src.wine.infrastructure.schema import WineCreate, WineUpdate


class WineRepository(WineRepositoryInterface):

    def init(self):
        self.db: Session = SessionLocal()

    def create(self, wine: WineCreate) -> Wine:
        db_wine = Wine(**wine.model_dump())

        self.db.add(db_wine)
        self.db.commit()
        self.db.refresh(db_wine)

        return db_wine

    def get_all(self) -> list[Wine]:
        return self.db.query(Wine).all()

    def get_by_id(self, wine_id: int) -> Wine | None:
        return (
            self.db.query(Wine)
            .filter(Wine.id == wine_id)
            .first()
        )

    def update(
        self,
        wine_id: int,
        wine: WineUpdate,
    ) -> Wine | None:

        db_wine = self.get_by_id(wine_id)

        if db_wine is None:
            return None

        data = wine.model_dump()

        for key, value in data.items():
            setattr(db_wine, key, value)

        self.db.commit()
        self.db.refresh(db_wine)

        return db_wine

    def delete(self, wine_id: int) -> bool:

        db_wine = self.get_by_id(wine_id)

        if db_wine is None:
            return False

        self.db.delete(db_wine)
        self.db.commit()

        return True

    def close(self):
        self.db.close()