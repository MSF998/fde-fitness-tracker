import subprocess
import sys
import os

if __name__ == "__main__":
    env = os.environ.copy()
    env["PYTHONPATH"] = "."
    
    print("Starting FastAPI backend...")
    backend = subprocess.Popen(
        ["uv", "run", "uvicorn", "backend.main:app", "--port", "8000"],
        env=env
    )
    
    print("Starting Streamlit frontend...")
    frontend = subprocess.Popen(
        ["uv", "run", "streamlit", "run", "frontend/app.py"],
        env=env
    )
    
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend.terminate()
        frontend.terminate()
        sys.exit(0)
