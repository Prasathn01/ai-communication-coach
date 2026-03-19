from fastapi import FastAPI

from app.routes.interview import router as interview_router
from app.routes.session import router as session_router

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(session_router)
app.include_router(interview_router)