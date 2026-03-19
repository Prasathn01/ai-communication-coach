from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

sessions = {}

INTERVIEW_QUESTIONS = [
    "Tell me about yourself.",
    "What are your strengths?",
    "Tell me about a project you worked on.",
    "Why should we hire you?",
    "Where do you see yourself in 3 years?"
]


class StartSessionResponse(BaseModel):
    session_id: str
    first_question: str


class AnswerRequest(BaseModel):
    session_id: str
    user_answer: str


class TurnFeedback(BaseModel):
    grammar: str
    vocabulary: str
    fluency: str


class InterviewResponse(BaseModel):
    ai_reply: str
    next_question: str | None
    turn_feedback: TurnFeedback
    question_number: int
    is_complete: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/session/start", response_model=StartSessionResponse)
def start_session():
    session_id = str(uuid4())

    sessions[session_id] = {
        "current_question_index": 0,
        "answers": []
    }

    return StartSessionResponse(
        session_id=session_id,
        first_question=INTERVIEW_QUESTIONS[0]
    )


@app.post("/interview/respond", response_model=InterviewResponse)
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
        ai_reply="Thanks for your answer. Let’s continue.",
        next_question=INTERVIEW_QUESTIONS[next_index],
        turn_feedback=feedback,
        question_number=next_index + 1,
        is_complete=False
    )