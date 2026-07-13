from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.shared.infrastructure.database import get_db

from src.feedback.infrastructure.repository import FeedbackRepository
from src.feedback.infrastructure.schema import (
    FeedbackCreate,
    FeedbackUpdate,
    FeedbackResponse,
)

from src.feedback.application.create_feedback import CreateFeedback
from src.feedback.application.get_all_feedback import GetAllFeedback
from src.feedback.application.get_feedback_by_id import GetFeedbackByid
from src.feedback.application.update_feedback import Updatefeedback
from src.feedback.application.delete_feedback import DeleteFeedback

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"],
)


@router.post("/", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
):
    repository = FeedbackRepository(db)

    created_feedback = CreateFeedback(repository).execute(feedback)

    return created_feedback


@router.get("/", response_model=list[FeedbackResponse])
def get_all_feedback(
    db: Session = Depends(get_db),
):
    repository = FeedbackRepository(db)

    feedback = GetAllFeedback(repository).execute()

    return feedback


@router.get("/{feedback_id}", response_model=FeedbackResponse)
def get_feedback_by_id(
    feedback_id: int,
    db: Session = Depends(get_db),
):
    repository = FeedbackRepository(db)

    feedback = GetFeedbackByid(repository).execute(feedback_id)

    if feedback is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Feedback not found",
        )

    return feedback


@router.put("/{feedback_id}", response_model=FeedbackResponse)
def update_feedback(
    feedback_id: int,
    feedback: FeedbackUpdate,
    db: Session = Depends(get_db),
):
    repository = FeedbackRepository(db)

    updated_feedback = Updatefeedback(repository).execute(
        feedback_id,
        feedback,
    )

    if updated_feedback is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Feedback not found",
        )

    return updated_feedback


@router.delete(
    "/{feedback_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_feedback(
    feedback_id: int,
    db: Session = Depends(get_db),
):
    repository = FeedbackRepository(db)

    deleted = DeleteFeedback(repository).execute(feedback_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Feedback not found",
        )

    return None