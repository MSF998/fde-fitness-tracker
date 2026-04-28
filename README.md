# AI Fitness Tracker

An AI-powered fitness tracker built with FastAPI (backend) and Streamlit (frontend).

## Architecture

- **Frontend**: Streamlit UI (`frontend/app.py`)
- **Backend**: FastAPI
  - `backend/main.py`: Entry point
  - `backend/api/`: API Routers and Dependencies
  - `backend/core/`: Configuration via `pydantic-settings`
  - `backend/schemas.py`: Pydantic Models
- **Database**: SQLite (`fitness.db`) via `backend/db_client.py`
- **AI**: Gemini API Integration (`backend/llm_service.py`)

## Setup & Running

1. **Install dependencies** (uses `uv`):
   ```bash
   uv sync
   ```

2. **Set environment variables**:
   Set `GEMINI_API_KEY` for AI features.
   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY="your-api-key"
   ```

3. **Run the App**:
   ```bash
   python run.py
   ```
   This starts the FastAPI backend (port 8000) and the Streamlit frontend.

## Testing

Tests are written using `pytest`. Run them with the python path set to the root directory.

```bash
$env:PYTHONPATH="."
uv run pytest
```
