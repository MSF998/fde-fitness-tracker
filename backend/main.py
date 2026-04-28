from fastapi import FastAPI
from backend.api.routers import profile, workout, generate

app = FastAPI()

app.include_router(profile.router)
app.include_router(workout.router)
app.include_router(generate.router)

@app.get("/ping")
def ping():
    return {"status": "ok"}
