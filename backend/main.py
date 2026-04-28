from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from backend.db_client import DBClient
from backend.llm_service import LLMService
import os

app = FastAPI()

def get_db():
    db = DBClient("fitness.db")
    db.init_db()
    return db

def get_llm():
    return LLMService(api_key=os.environ.get("GEMINI_API_KEY", "dummy"))

class Profile(BaseModel):
    name: str
    goal: str

class Workout(BaseModel):
    user_id: int
    type: str
    duration: int
    calories: int

class GenerateRequest(BaseModel):
    user_id: int

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/profile")
def create_profile(profile: Profile, db: DBClient = Depends(get_db)):
    user_id = db.save_profile(profile.model_dump())
    return {"id": user_id}

@app.post("/workout")
def log_workout(workout: Workout, db: DBClient = Depends(get_db)):
    log_id = db.log_workout(workout.model_dump())
    return {"id": log_id}

@app.post("/generate")
def generate_plan(req: GenerateRequest, db: DBClient = Depends(get_db), llm: LLMService = Depends(get_llm)):
    profile = db.get_profile(req.user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    safe, reason = llm.check_safety(profile["goal"])
    if not safe:
        raise HTTPException(status_code=400, detail=f"Unsafe goal: {reason}")
    
    plan = llm.generate_plan(profile)
    return {"plan": plan}
