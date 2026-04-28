## Problem Statement
Users need personalized fitness guidance, activity tracking, and intelligent recommendations, but lack a unified, safe, and easy-to-use platform that adapts to their progress.

## Solution
A Streamlit frontend + FastAPI backend application that logs workouts, sets goals, and provides AI-driven fitness recommendations using OpenAI. It includes rule-based safety guardrails to prevent harmful advice.

## User Stories
1. As a user, I want to create a profile with my fitness goals, so that the AI can give personalized advice.
2. As a user, I want to log my daily workouts, so that I can track my activity over time.
3. As a user, I want to view a dashboard of my progress, so that I can stay motivated.
4. As a user, I want to click a "Generate Plan" button, so that I receive AI-tailored workout suggestions.
5. As a user, I want to chat with the AI about fitness, so that I can ask specific health questions.
6. As a system administrator, I want rule-based safety guardrails, so that users do not receive dangerous workout or diet advice.

## Implementation Decisions
- Monorepo structure (`backend/` for FastAPI, `frontend/` for Streamlit).
- SQLite for database.
- Single mock user authentication for MVP.
- Direct integration with OpenAI API for recommendations.
- `db_client`: Deep module for SQLite operations.
- `llm_service`: Deep module for OpenAI calls and system-prompt guardrails.
- Rule-based safety (e.g. max weight limits, disallowed keywords) enforced in backend before AI calls.

## Testing Decisions
- Test external behavior, not implementation details.
- Modules to be tested: `db_client` (database CRUD), `llm_service` (AI safety rules and valid prompt generation).

## Out of Scope
- Multi-user real authentication (JWT, OAuth).
- Real-time wearable data sync.
- Production deployment (Docker, cloud hosting) for now.

## Further Notes
- Add `pytest` for backend testing.
