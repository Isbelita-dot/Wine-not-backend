from src.feedback.domain.repository import FeedbackRepositoryInterface
from src.feedback.infrastructure.model import Feedback

class GetAllFeedback:

    def __init__(self, repository:FeedbackRepositoryInterface):
        self.repository = repository

    def execute(self) -> list[Feedback]:
        return self.repository.get_all()