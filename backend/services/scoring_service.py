from app.models.schemas import FinalReportResponse


def generate_mock_final_report(total_answers: int) -> FinalReportResponse:
    return FinalReportResponse(
        overall_score=74,
        grammar_score=78,
        vocabulary_score=69,
        fluency_score=73,
        top_mistakes=[
            "Answers are too short",
            "Vocabulary is too general",
            "Professional examples need improvement"
        ],
        roadmap=[
            "Practice introducing yourself in 4 to 5 structured sentences",
            "Use stronger project-related vocabulary",
            "Answer using situation, action, result format"
        ],
        total_answers=total_answers
    )