## Problem Statement
The codebase contains hardcoded configuration values (database path, AI model names, API URLs) scattered across various files. This makes it difficult to deploy the app to different environments or change configurations without modifying code.

## Solution
Centralize configuration management by moving all hardcoded values to environment variables loaded via `.env` files. We will expand the existing `pydantic-settings` setup in the backend and introduce environment variable usage in the frontend.

## Commits
1. **Backend Config**: Add `DATABASE_URL` and `GEMINI_MODEL` to `backend/core/config.py`. Update `backend/api/dependencies.py` to use `settings.database_url`. Update `backend/llm_service.py` to accept the model name and use it in generation.
2. **Frontend Config**: Update `frontend/app.py` to load `API_URL` from the environment (`os.getenv`), defaulting to `http://localhost:8000`.

## Decision Document
- **Modules**: `backend.core.config`, `backend.api.dependencies`, `backend.llm_service`, `frontend.app`
- **Configuration**:
  - `DATABASE_URL` (default: "fitness.db")
  - `GEMINI_MODEL` (default: "gemini-2.5-flash")
  - `API_URL` (default: "http://localhost:8000")
- **Interfaces**: Modifying `LLMService.__init__` to accept `model_name`.

## Testing Decisions
- Testing behavior remains unchanged. The existing `pytest` suite will verify that the app functions correctly with the default configuration values.
- Dependency overrides in tests will naturally isolate the test DB path.

## Out of Scope
- Creating deployment-specific files (e.g., Dockerfiles).
- Refactoring internal business logic.
