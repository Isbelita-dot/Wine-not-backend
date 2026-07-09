from sqlalchemy.orm import Session

from src.feedback.domain.repository import FeedbackRepositoryInterface
from src.feedback.infrastructure.model import Feedback
from src.feedback.infrastructure.schema import (
    FeedbackCreate,
    FeedbackUpdate,
)


class FeedbackRepository(FeedbackRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        feedback: FeedbackCreate,
    ) -> Feedback:

        db_feedback = Feedback(
            customer_name=feedback.customer_name,
            email=feedback.email,
            rating=feedback.rating,
            comment=feedback.comment,
            wine_id=feedback.wine_id,
        )

        self.db.add(db_feedback)
        self.db.commit()
        self.db.refresh(db_feedback)

        return db_feedback

    def get_all(self) -> list[Feedback]:
        return self.db.query(Feedback).all()

    def get_by_id(
        self,
        feedback_id: int,
    ) -> Feedback | None:

        return (
            self.db.query(Feedback)
            .filter(Feedback.id == feedback_id)
            .first()
        )

    def update(
        self,
        feedback_id: int,
        feedback: FeedbackUpdate,
    ) -> Feedback | None:

        db_feedback = self.get_by_id(feedback_id)

        if db_feedback is None:
            return None

        db_feedback.customer_name = feedback.customer_name
        db_feedback.email = feedback.email
        db_feedback.rating = feedback.rating
        db_feedback.comment = feedback.comment
        db_feedback.wine_id = feedback.wine_id

        self.db.commit()
        self.db.refresh(db_feedback)

        return db_feedback

    def delete(
        self,
        feedback_id: int,
    ) -> bool:

        db_feedback = self.get_by_id(feedback_id)

        if db_feedback is None:
            return False

        self.db.delete(db_feedback)
        self.db.commit()

        return True