from streamlit.testing.v1 import AppTest
from unittest.mock import patch

def test_app_loads():
    at = AppTest.from_file("frontend/app.py")
    at.run()
    assert not at.exception
    assert len(at.title) > 0
    assert at.title[0].value == "Fitness Tracker"

@patch("frontend.app.requests.post")
def test_profile_form(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"id": 1}

    at = AppTest.from_file("frontend/app.py")
    at.run()
    
    at.text_input(key="profile_name").input("Bob")
    at.text_input(key="profile_goal").input("gain muscle")
    at.button(key="submit_profile").click()
    at.run()

    mock_post.assert_called_once_with(
        "http://localhost:8000/profile",
        json={"name": "Bob", "goal": "gain muscle"}
    )
    assert len(at.success) > 0
    assert "ID: 1" in at.success[0].value

@patch("frontend.app.requests.post")
def test_workout_form(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"id": 1}

    at = AppTest.from_file("frontend/app.py")
    at.run()
    
    at.number_input(key="workout_user_id").set_value(1)
    at.text_input(key="workout_type").input("running")
    at.number_input(key="workout_duration").set_value(30)
    at.number_input(key="workout_calories").set_value(300)
    at.button(key="submit_workout").click()
    at.run()

    mock_post.assert_called_with(
        "http://localhost:8000/workout",
        json={"user_id": 1, "type": "running", "duration": 30, "calories": 300}
    )
    assert len(at.success) > 0
    assert any("Workout logged! ID: 1" in s.value for s in at.success)

@patch("frontend.app.requests.post")
def test_generate_plan_form(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"plan": "Do 10 pushups"}

    at = AppTest.from_file("frontend/app.py")
    at.run()
    
    at.number_input(key="generate_user_id").set_value(1)
    at.button(key="submit_generate").click()
    at.run()

    mock_post.assert_called_with(
        "http://localhost:8000/generate",
        json={"user_id": 1}
    )
    assert len(at.success) > 0
    assert any("Plan: Do 10 pushups" in s.value for s in at.success)
