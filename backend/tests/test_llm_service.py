from unittest.mock import patch
from backend.llm_service import LLMService

def test_check_safety_rejects_extreme_loss():
    service = LLMService(api_key="dummy")
    safe, reason = service.check_safety("I want to lose 50 lbs in a week")
    assert not safe
    assert "rate" in reason.lower()

def test_check_safety_accepts_normal_goal():
    service = LLMService(api_key="dummy")
    safe, reason = service.check_safety("I want to get stronger legs")
    assert safe
    assert reason == ""

@patch("backend.llm_service.genai")
def test_generate_plan(mock_genai):
    mock_client = mock_genai.Client.return_value
    mock_response = mock_client.models.generate_content.return_value
    mock_response.text = "Here is your plan: Do 10 pushups."

    service = LLMService(api_key="dummy")
    plan = service.generate_plan({"name": "Bob", "goal": "strength"})
    
    assert plan is not None
    assert "pushups" in plan.lower()
    mock_client.models.generate_content.assert_called_once()
