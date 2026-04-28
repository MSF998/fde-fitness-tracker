## Problem Statement
The backend code currently sits mostly in `main.py`, including Pydantic models, FastAPI routes, and configuration setup. As the application grows, this will become difficult to maintain. Additionally, configuration is handled via raw `os.environ` instead of a dedicated `.env` configuration file, which makes local development less structured.

## Solution
Organize the backend into a modular architecture:
1. Extract Pydantic models into a dedicated `schemas.py` file.
2. Implement `pydantic-settings` to load configuration from a `.env` file.
3. Split FastAPI endpoints from `main.py` into dedicated routers inside `backend/api/routers/`.

## Commits
1. **Extract Schemas**: Create `backend/schemas.py` and move `Profile`, `Workout`, and `GenerateRequest` models there. Update imports in `main.py`.
2. **Setup Config**: Add `pydantic-settings`. Create `backend/core/config.py` to handle `.env` loading for `GEMINI_API_KEY`. Update `main.py` to use it.
3. **Modular Routers**: Create `backend/api/routers/profile.py`, `backend/api/routers/workout.py`, and `backend/api/routers/generate.py`. Move corresponding endpoints from `main.py` to these routers. Register routers in `main.py`.

## Decision Document
- **Modules**: `backend.schemas`, `backend.core.config`, `backend.api.routers.*`
- **Interfaces**: API contracts and JSON schemas remain identical.
- **Architectural decisions**: Standard FastAPI layered architecture (Models/Schemas separated from Routers).
- **Configuration**: Use `.env` file via `pydantic-settings` for strongly-typed config.

## Testing Decisions
- Testing will remain black-box HTTP testing via `fastapi.testclient.TestClient`.
- The existing tests in `backend/tests/test_api.py` will serve as the verification that the refactor did not break the public interface.
- No new tests are strictly necessary since behavior is unchanged.

## Out of Scope
- Refactoring `db_client.py` or `llm_service.py` internals.
- Adding new endpoints or modifying the UI.
