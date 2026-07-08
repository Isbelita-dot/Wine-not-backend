from datetime import datetime

from pydantic import EmailStr, Field

from src.shared.infrastructure.schema import BaseSchema


class FeedbackBase(BaseSchema):
    customer_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["Marc"],
    )

    email: EmailStr = Field(
        ...,
        examples=["marc@gmail.com"],
    )

    rating: int = Field(
        ...,
        ge=1,
        le=5,
        examples=[5],
    )

    comment: str = Field(
        ...,
        min_length=5,
        max_length=500,
        examples=["Vino intenso pero con un toque dulce, recomendable."],
    )

    wine_id: int = Field(
        ...,
        gt=0,
        examples=[1],
    )


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(FeedbackBase):
    pass


class FeedbackResponse(FeedbackBase):
    id: int
    created_at: datetime