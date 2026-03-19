from fastapi import APIRouter, HTTPException

from app.models.schemas import AnswerRequest, InterviewResponse, TurnFeedback
from app.routes.session import INTERVIEW_QUESTIONS, sessions

router = APIRouter()


@router.post("/interview/respond", response_model=InterviewResponse)
def respond_to_interview(answer: AnswerRequest):
    session = sessions.get(answer.session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    current_index = session["current_question_index"]

    if current_index >= len(INTERVIEW_QUESTIONS):
        raise HTTPException(status_code=400, detail="Interview already completed")

    session["answers"].append({
        "question": INTERVIEW_QUESTIONS[current_index],
        "answer": answer.user_answer
    })

    feedback = TurnFeedback(
        grammar="Mostly clear sentence structure.",
        vocabulary="Try to use more professional and specific words.",
        fluency="Good start. Try to answer in a slightly more structured way."
    )

    next_index = current_index + 1
    is_complete = next_index >= len(INTERVIEW_QUESTIONS)

    session["current_question_index"] = next_index

    if is_complete:
        return InterviewResponse(
            ai_reply="Thank you. That completes the interview session.",
            next_question=None,
            turn_feedback=feedback,
            question_number=next_index,
            is_complete=True
        )

    return InterviewResponse(
        ai_reply="Thanks for your answer. Let's continue.",
        next_question=INTERVIEW_QUESTIONS[next_index],
        turn_feedback=feedback,
        question_number=next_index + 1,
        is_complete=False
    )