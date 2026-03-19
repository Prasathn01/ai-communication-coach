import json

from app.models.schemas import TurnFeedback


def generate_mock_turn_feedback(user_answer: str) -> TurnFeedback:
    answer_length = len(user_answer.strip().split())

    if answer_length < 8:
        return TurnFeedback(
            grammar="Sentence is understandable, but the answer is too short.",
            vocabulary="Use more specific and professional words.",
            fluency="Try to explain your idea in 2 to 4 complete sentences."
        )

    return TurnFeedback(
        grammar="Grammar is mostly clear with minor improvement possible.",
        vocabulary="Good start. You can make the answer more professional and precise.",
        fluency="Reasonably fluent answer. Add a stronger structure."
    )


def generate_mock_final_feedback_payload(session_answers: list[dict]) -> dict:
    total_answers = len(session_answers)

    return {
        "overall_score": 76,
        "grammar_score": 79,
        "vocabulary_score": 72,
        "fluency_score": 77,
        "top_mistakes": [
            "Answers are not detailed enough",
            "Vocabulary can be more role-specific",
            "Examples are not strong enough"
        ],
        "roadmap": [
            "Answer in 3 to 5 structured sentences",
            "Use more technical and professional vocabulary",
            "Support answers with one concrete example"
        ],
        "total_answers": total_answers
    }