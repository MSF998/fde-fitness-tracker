import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("Fitness Tracker")

st.header("Profile Setup")
name = st.text_input("Name", key="profile_name")
goal = st.text_input("Goal", key="profile_goal")

if st.button("Save Profile", key="submit_profile"):
    response = requests.post(f"{API_URL}/profile", json={"name": name, "goal": goal})
    if response.status_code == 200:
        data = response.json()
        st.success(f"Profile saved! ID: {data['id']}")
    else:
        st.error("Failed to save profile")

st.header("Log Workout")
w_user_id = st.number_input("User ID for Workout", min_value=1, step=1, key="workout_user_id")
w_type = st.text_input("Workout Type", key="workout_type")
w_duration = st.number_input("Duration (min)", min_value=1, step=1, key="workout_duration")
w_calories = st.number_input("Calories", min_value=1, step=1, key="workout_calories")

if st.button("Log Workout", key="submit_workout"):
    payload = {
        "user_id": w_user_id,
        "type": w_type,
        "duration": w_duration,
        "calories": w_calories
    }
    response = requests.post(f"{API_URL}/workout", json=payload)
    if response.status_code == 200:
        data = response.json()
        st.success(f"Workout logged! ID: {data['id']}")
    else:
        st.error("Failed to log workout")

st.header("Generate AI Plan")
g_user_id = st.number_input("User ID for Plan", min_value=1, step=1, key="generate_user_id")

if st.button("Generate Plan", key="submit_generate"):
    response = requests.post(f"{API_URL}/generate", json={"user_id": g_user_id})
    if response.status_code == 200:
        data = response.json()
        st.success(f"Plan: {data['plan']}")
    else:
        st.error(f"Failed to generate plan: {response.text}")
