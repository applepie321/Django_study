from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list")
def question_list():
    db = SessionLocal()
    _qustion_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _qustion_list