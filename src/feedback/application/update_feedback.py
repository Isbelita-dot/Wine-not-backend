from src.feedback.domain.repository import FeedbackRepositoryInterface
from src.feedback.infrastructure.model import Feedback
from src.feedback.infrastructure.schema import FeedbackUpdate


class Updatefeedback:

    def __init__(self, repository: FeedbackRepositoryInterface):
        self.repository = repository

    def execute(
        self,
        feedback_id: int,
        feedback: FeedbackUpdate,
    ) -> Feedback | None:
        return self.repository.update(feedback_id, feedback)