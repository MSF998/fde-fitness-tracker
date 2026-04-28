from pydantic import BaseModel

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
