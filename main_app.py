
import streamlit as st
import json
import importlib

ROLE_TOOLS = {
    "admin": {
        "🩺 Injury Log": "modules.ops.injury_log_ai",
        "🙋 Waiver Tracker": "modules.ops.volunteer_waiver_tracker",
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner",
        "📅 Trainer Scheduler": "modules.ops.trainer_schedule_ai",
        "📋 Game Checklist": "modules.ops.game_day_checklist"
    },
    "referee": {
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner"
    },
    "medical_staff": {
        "🩺 Injury Log": "modules.ops.injury_log_ai",
        "📅 Trainer Scheduler": "modules.ops.trainer_schedule_ai"
    },
    "volunteer": {
        "🙋 Waiver Tracker": "modules.ops.volunteer_waiver_tracker"
    },
    "scheduler_admin": {
        "📋 Game Checklist": "modules.ops.game_day_checklist"
    },
    "event_ops": {
        "📋 Game Checklist": "modules.ops.game_day_checklist"
    }
}

def login():
    st.sidebar.header("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        with open("users.json") as f:
            users = json.load(f)
        user = users.get(email)
        if user and user["password"] == password:
            st.session_state.user = {"email": email, "role": user["role"]}
        else:
            st.sidebar.error("Invalid credentials.")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.user = None

def run():
    st.set_page_config(page_title="SportAI Ops Dashboard", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools available for your role.")
        return
    selection = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if selection:
        try:
            mod = importlib.import_module(tools[selection])
            mod.run()
        except Exception as e:
            st.error(f"Tool failed to run: {e}")

run()
