from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app, get_db
from backend.db_client import DBClient

# Use in-memory DB for tests
_test_db = DBClient(":memory:")
_test_db.init_db()

def override_get_db():
    return _test_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_profile():
    profile_data = {"name": "Bob", "goal": "gain muscle"}
    response = client.post("/profile", json=profile_data)
    
    assert response.status_code == 200
    assert "id" in response.json()

def test_log_workout():
    workout_data = {
        "user_id": 1,
        "type": "running",
        "duration": 30,
        "calories": 300
    }
    response = client.post("/workout", json=workout_data)
    
    assert response.status_code == 200
    assert "id" in response.json()

@patch("backend.main.LLMService")
def test_generate_plan_api(mock_llm_class):
    mock_llm = mock_llm_class.return_value
    mock_llm.check_safety.return_value = (True, "")
    mock_llm.generate_plan.return_value = "Test plan: 10 pushups"

    profile_data = {"name": "Charlie", "goal": "strength"}
    resp = client.post("/profile", json=profile_data)
    user_id = resp.json()["id"]

    response = client.post("/generate", json={"user_id": user_id})
    assert response.status_code == 200
    assert "pushups" in response.json()["plan"]
