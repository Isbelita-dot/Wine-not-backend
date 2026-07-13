from src.feedback.domain.repository import FeedbackRepositoryInterface
from src.feedback.infrastructure.model import Feedback
from src.feedback.infrastructure.schema import FeedbackCreate


class CreateFeedback:

    def __init__(
        self,
        repository: FeedbackRepositoryInterface,
    ):
        self.repository = repository

    def execute(
        self,
        feedback: FeedbackCreate,
    ) -> Feedback:

        return self.repository.create(feedback)