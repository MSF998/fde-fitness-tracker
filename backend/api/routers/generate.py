from fastapi import APIRouter, Depends, HTTPException
from backend.schemas import GenerateRequest, ChatRequest
from backend.db_client import DBClient
from backend.llm_service import LLMService
from backend.api.dependencies import get_db, get_llm

router = APIRouter()

@router.post("/generate")
def generate_plan(req: GenerateRequest, db: DBClient = Depends(get_db), llm: LLMService = Depends(get_llm)):
    profile = db.get_profile(req.user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    safe, reason = llm.check_safety(profile["goal"])
    if not safe:
        raise HTTPException(status_code=400, detail=f"Unsafe goal: {reason}")
    
    plan = llm.generate_plan(profile)
    return {"plan": plan}

@router.post("/chat")
def chat_api(req: ChatRequest, db: DBClient = Depends(get_db), llm: LLMService = Depends(get_llm)):
    profile = db.get_profile(req.user_id)
    workouts = db.get_user_workouts(req.user_id)
    response_text = llm.chat(message=req.message, profile=profile, workouts=workouts)
    return {"response": response_text}
