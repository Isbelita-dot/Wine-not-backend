from pydantic import Field

from src.shared.infrastructure.schema import BaseSchema
from src.category.infrastructure.schema import CategoryResponse


class WineBase(BaseSchema):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Rioja Reserva"],
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500,
        examples=["Reserva con notas de frutos rojos."],
    )

    winery: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Marqués de Cáceres"],
    )

    grape: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Tempranillo"],
    )

    rating: float = Field(
        ...,
        ge=0,
        le=5,
        examples=[4.8],
    )

    badge: str = Field(
        ...,
        max_length=50,
        examples=["Reserva"],
    )

    price: float = Field(
        ...,
        gt=0,
        examples=[18.90],
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
        examples=["Rioja"],
    )

    year: int = Field(
        ...,
        ge=1900,
        le=2026,
        examples=[2020],
    )

    image_url: str = Field(
        ...,
        examples=["./assets/images/products/rioja-reserva.png"],
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