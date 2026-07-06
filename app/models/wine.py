from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base

class Wine(Base):
    __tablename__ = "wines"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    region: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    image_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    category_id: Mapped[str] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="wines"
    )

    feedbacks: Mapped[list["Feedback"]] = relationship(
        back_populates="wine",
        cascade="all, delete-orphan"
    )