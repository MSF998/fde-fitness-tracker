import pytest
from backend.db_client import DBClient

def test_save_profile_makes_it_retrievable():
    db = DBClient(":memory:")
    db.init_db()
    
    profile_data = {"name": "Alice", "goal": "lose weight"}
    user_id = db.save_profile(profile_data)
    
    retrieved = db.get_profile(user_id)
    assert retrieved["name"] == "Alice"
    assert retrieved["goal"] == "lose weight"

def test_log_workout_makes_it_retrievable():
    db = DBClient(":memory:")
    db.init_db()
    
    workout_data = {
        "user_id": 1, 
        "type": "running", 
        "duration": 30, 
        "calories": 300
    }
    log_id = db.log_workout(workout_data)
    
    retrieved = db.get_workout(log_id)
    assert retrieved["type"] == "running"
    assert retrieved["duration"] == 30
    assert retrieved["calories"] == 300
