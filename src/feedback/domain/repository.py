from abc import ABC, abstractmethod

from src.feedback.infrastructure.model import Feedback
from src.feedback.infrastructure.schema import (
    FeedbackCreate,
    FeedbackUpdate,
)


class FeedbackRepositoryInterface(ABC):

    @abstractmethod
    def create(
        self,
        feedback: FeedbackCreate,
    ) -> Feedback:
        pass

    @abstractmethod
    def get_all(self) -> list[Feedback]:
        pass

    @abstractmethod
    def get_by_id(
        self,
        feedback_id: int,
    ) -> Feedback | None:
        pass

    @abstractmethod
    def update(
        self,
        feedback_id: int,
        feedback: FeedbackUpdate,
    ) -> Feedback | None:
        pass

    @abstractmethod
    def delete(
        self,
        feedback_id: int,
    ) -> bool:
        pass