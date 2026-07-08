from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.infrastructure.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    rating: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    comment: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    wine_id: Mapped[int] = mapped_column(
        ForeignKey("wines.id"),
        nullable=False
    )

    wine: Mapped["Wine"] = relationship(
        back_populates="feedbacks"
    )

