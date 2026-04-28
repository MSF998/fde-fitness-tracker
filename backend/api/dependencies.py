from backend.db_client import DBClient
from backend.llm_service import LLMService
from backend.core.config import settings

def get_db():
    db = DBClient("fitness.db")
    db.init_db()
    return db

def get_llm():
    return LLMService(api_key=settings.gemini_api_key)
