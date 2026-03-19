from app.models.schemas import FinalReportResponse
from app.services.llm_service import generate_mock_final_feedback_payload


def generate_mock_final_report(session_answers: list[dict]) -> FinalReportResponse:
    payload = generate_mock_final_feedback_payload(session_answers)
    return FinalReportResponse(**payload)