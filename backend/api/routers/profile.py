from fastapi import APIRouter, Depends
from backend.schemas import Profile
from backend.db_client import DBClient
from backend.api.dependencies import get_db

router = APIRouter()

@router.post("/profile")
def create_profile(profile: Profile, db: DBClient = Depends(get_db)):
    user_id = db.save_profile(profile.model_dump())
    return {"id": user_id}
