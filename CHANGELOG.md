# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Modular backend architecture with FastAPI (`APIRouter`, schemas, dependencies)
- Centralized configuration system using `pydantic-settings` and `.env` files
- Integration with Gemini API for fitness plan generation (`google-genai`)
- Initial Streamlit frontend with Profile, Workout, and Generate UI forms
- SQLite database wrapper for simple persistance (`fitness.db`)
- Pytest suite for end-to-end and component testing
