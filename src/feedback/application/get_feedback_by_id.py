from src.feedback.domain.repository import FeedbackRepositoryInterface
from src.feedback.infrastructure.model import Feedback

class GetFeedbackByid:
    
    def __init__(self, repository: FeedbackRepositoryInterface):
        self.repository = repository

    def execute(self, feedback_id: int) -> Feedback | None:
        return self.repository.get_by_id(feedback_id)