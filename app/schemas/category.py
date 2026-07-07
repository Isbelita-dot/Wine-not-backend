from pydantic import Field

from app.schemas.base import BaseSchema

class CategoryBase(BaseSchema):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Tinto"],
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=255,
        examples=["Vino rojo con sabor intenso."],
    )

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int