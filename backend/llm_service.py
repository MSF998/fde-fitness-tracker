import re
from google import genai

class LLMService:
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key
        self.model_name = model_name

    def check_safety(self, prompt: str) -> tuple[bool, str]:
        prompt_lower = prompt.lower()
        if "lose" in prompt_lower and "week" in prompt_lower:
            nums = re.findall(r'\d+', prompt_lower)
            if any(int(n) > 5 for n in nums):
                return False, "Unsafe rate of weight loss requested. Maximum safe rate is 1-2 lbs/week."
        
        return True, ""

    def generate_plan(self, profile: dict) -> str:
        client = genai.Client(api_key=self.api_key)
        prompt = f"Create a workout plan for {profile.get('name')} whose goal is {profile.get('goal')}."
        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text

    def chat(self, message: str, profile: dict, workouts: list[dict]) -> str:
        is_safe, reason = self.check_safety(message)
        if not is_safe:
            return reason
            
        from google import genai
        client = genai.Client(api_key=self.api_key)
        context = f"User Profile: {profile}. Workouts: {workouts}."
        prompt = f"Context: {context}\nUser Question: {message}\nAnswer as a helpful fitness assistant."
        
        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text
