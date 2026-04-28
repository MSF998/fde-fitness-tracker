$body1 = @"
## What to build
FastAPI ping Streamlit end-to-end setup.

## Acceptance criteria
- [ ] FastAPI runs on port 8000
- [ ] Streamlit runs on port 8501
- [ ] Streamlit calls FastAPI ping endpoint successfully

## Blocked by
None - can start immediately
"@
gh issue create --title "[AFK] 1. Setup Skeleton" --body $body1

$body2 = @"
## What to build
SQLite schema, API endpoint, and UI form for user profile.

## Acceptance criteria
- [ ] SQLite DB initializes
- [ ] POST /profile saves user
- [ ] Streamlit form submits profile data

## Blocked by
- Blocked by #1
"@
gh issue create --title "[AFK] 2. Profile Create" --body $body2

$body3 = @"
## What to build
SQLite schema, API endpoint, and UI form for workout logs.

## Acceptance criteria
- [ ] POST /workout saves log
- [ ] Streamlit form submits workout data

## Blocked by
- Blocked by #2
"@
gh issue create --title "[AFK] 3. Workout Log" --body $body3

$body4 = @"
## What to build
Dashboard UI fetching stats from API.

## Acceptance criteria
- [ ] GET /stats aggregates data
- [ ] UI chart displays stats
- [ ] Human review of UI layout

## Blocked by
- Blocked by #3
"@
gh issue create --title "[HITL] 4. Progress Dash" --body $body4

$body5 = @"
## What to build
OpenAI config and guardrails with prompt tests.

## Acceptance criteria
- [ ] OpenAI client configured
- [ ] Guardrails reject bad input
- [ ] Human review of system prompts

## Blocked by
- Blocked by #1
"@
gh issue create --title "[HITL] 5. LLM Safety Setup" --body $body5

$body6 = @"
## What to build
API logic for plan generation connected to UI button.

## Acceptance criteria
- [ ] POST /generate returns workout plan
- [ ] UI button calls API and displays plan

## Blocked by
- Blocked by #2
- Blocked by #5
"@
gh issue create --title "[AFK] 6. Generate Plan" --body $body6

$body7 = @"
## What to build
API chat logic connected to UI chat component.

## Acceptance criteria
- [ ] POST /chat handles messages
- [ ] UI provides chat interface

## Blocked by
- Blocked by #5
"@
gh issue create --title "[AFK] 7. AI Chat" --body $body7
