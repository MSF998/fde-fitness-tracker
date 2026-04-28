from fastapi import APIRouter, Depends
from backend.schemas import Workout
from backend.db_client import DBClient
from backend.api.dependencies import get_db

router = APIRouter()

@router.post("/workout")
def log_workout(workout: Workout, db: DBClient = Depends(get_db)):
    log_id = db.log_workout(workout.model_dump())
    return {"id": log_id}
