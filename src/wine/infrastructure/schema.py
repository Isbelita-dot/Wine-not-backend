from pydantic import Field

from src.shared.infrastructure.schema import BaseSchema
from src.category.infrastructure.schema import CategoryResponse


class WineBase(BaseSchema):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Rioja"],
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=255,
        examples=["Reserva con notas de frutos rojos."],
    )

    price: float = Field(
        ...,
        gt=0,
        examples=[25],
    )

    stock: int = Field(
        ...,
        ge=0,
        examples=[20],
    )

    country: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["España"],
    )

    region: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["La Rioja"],
    )

    year: int = Field(
        ...,
        ge=1900,
        le=2026,
        examples=[2020],
    )

    image_url: str = Field(
        ...,
        examples=["https://example.com/image/rioja.jpg"],
    )

    category_id: int = Field(
        ...,
        gt=0,
        examples=[1],
    )


class WineCreate(WineBase):
    pass


class WineUpdate(WineBase):
    pass


class WineResponse(WineBase):
    id: int
    category: CategoryResponse