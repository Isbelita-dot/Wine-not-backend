from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.shared.infrastructure.database import get_db

from src.wine.infrastructure.repository import WineRepository
from src.wine.infrastructure.schema import (
    WineCreate,
    WineResponse,
    WineUpdate,
)

from src.wine.application.create_wine import CreateWine
from src.wine.application.get_all_wines import GetAllWines
from src.wine.application.get_wine_by_id import GetWineById
from src.wine.application.update_wine import UpdateWine
from src.wine.application.delete_wine import DeleteWine


router = APIRouter(
    prefix="/wines",
    tags=["Wines"],
)


@router.post(
    "/",
    response_model=WineResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_wine(
    wine: WineCreate,
    db: Session = Depends(get_db),
):
    repository = WineRepository(db)
    use_case = CreateWine(repository)

    return use_case.execute(wine)


@router.get(
    "/",
    response_model=list[WineResponse],
)
def get_all_wines(
    db: Session = Depends(get_db),
):
    repository = WineRepository(db)
    use_case = GetAllWines(repository)

    return use_case.execute()


@router.get(
    "/{wine_id}",
    response_model=WineResponse,
)
def get_wine_by_id(
    wine_id: int,
    db: Session = Depends(get_db),
):
    repository = WineRepository(db)
    use_case = GetWineById(repository)

    wine = use_case.execute(wine_id)

    if wine is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wine not found",
        )

    return wine
@router.put(
    "/{wine_id}",
    response_model=WineResponse,
)
def update_wine(
    wine_id: int,
    wine: WineUpdate,
    db: Session = Depends(get_db),
):
    repository = WineRepository(db)
    use_case = UpdateWine(repository)

    updated = use_case.execute(
        wine_id,
        wine,
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wine not found",
        )

    return updated


@router.delete(
    "/{wine_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_wine(
    wine_id: int,
    db: Session = Depends(get_db),
):
    repository = WineRepository(db)
    use_case = DeleteWine(repository)

    deleted = use_case.execute(wine_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wine not found",
        )

    return None