from pydantic import BaseModel


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


class EndSessionRequest(BaseModel):
    session_id: str


class FinalReportResponse(BaseModel):
    overall_score: int
    grammar_score: int
    vocabulary_score: int
    fluency_score: int
    top_mistakes: list[str]
    roadmap: list[str]
    total_answers: int