from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.shared.infrastructure.database import get_db

from src.category.infrastructure.repository import CategoryRepository
from src.category.infrastructure.schema import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)

from src.category.application.create_category import CreateCategory
from src.category.application.get_all_categories import GetAllCategories
from src.category.application.get_category_by_id import GetCategoryById
from src.category.application.update_category import UpdateCategory
from src.category.application.delete_category import DeleteCategory


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    created_category = CreateCategory(repository).execute(category)

    return created_category


@router.get("/",response_model=list[CategoryResponse])
def get_all_categories(
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    categories = GetAllCategories(repository).execute()

    return categories


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category_by_id(
    category_id: int,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    category = GetCategoryById(repository).execute(category_id)

    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return category


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    updated_category = UpdateCategory(repository).execute(
        category_id,
        category,
    )

    if updated_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return updated_category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    repository = CategoryRepository(db)

    deleted = DeleteCategory(repository).execute(category_id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Category not found")

    return None