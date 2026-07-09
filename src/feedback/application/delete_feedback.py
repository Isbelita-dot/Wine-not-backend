from src.feedback.domain.repository import FeedbackRepositoryInterface

class DeleteFeedback:

    def __init__(self, repository: FeedbackRepositoryInterface):
        self.repository = repository

    def execute(self, feedback_id: int) -> bool:
        return self.repository.delete(feedback_id)