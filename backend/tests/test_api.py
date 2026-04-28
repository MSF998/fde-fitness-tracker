from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app
from backend.api.dependencies import get_db
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

from unittest.mock import MagicMock
from backend.api.dependencies import get_llm

def override_get_llm():
    mock_llm = MagicMock()
    mock_llm.check_safety.return_value = (True, "")
    mock_llm.generate_plan.return_value = "Test plan: 10 pushups"
    mock_llm.chat.return_value = "Eat in a deficit."
    return mock_llm

app.dependency_overrides[get_llm] = override_get_llm

def test_generate_plan_api():
    profile_data = {"name": "Charlie", "goal": "strength"}
    resp = client.post("/profile", json=profile_data)
    user_id = resp.json()["id"]

    response = client.post("/generate", json={"user_id": user_id})
    assert response.status_code == 200
    assert "pushups" in response.json()["plan"]

def test_get_user_workouts():
    profile_data = {"name": "Dave", "goal": "cardio"}
    resp = client.post("/profile", json=profile_data)
    user_id = resp.json()["id"]

    workout_data = {"user_id": user_id, "type": "cycling", "duration": 45, "calories": 400}
    client.post("/workout", json=workout_data)

    resp = client.get(f"/workouts/{user_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["type"] == "cycling"

def test_chat_api():
    profile_data = {"name": "Evan", "goal": "fat loss"}
    resp = client.post("/profile", json=profile_data)
    user_id = resp.json()["id"]

    chat_data = {"user_id": user_id, "message": "How to burn belly fat?"}
    response = client.post("/chat", json=chat_data)
    assert response.status_code == 200
    assert "response" in response.json()
    assert "deficit" in response.json()["response"]
