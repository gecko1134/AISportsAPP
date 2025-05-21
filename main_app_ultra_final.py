
import streamlit as st
import json
from modules.ai.training_plan_optimizer import run as training_run
from modules.ai.event_sponsorship_matcher import run as sponsorship_run
from modules.ai.multi_sport_demand_predictor import run as demand_run
from modules.ai.youth_engagement_tracker import run as youth_run
from modules.ai.scholarship_probability_ai import run as scholarship_run
from modules.ai.email_response_predictor import run as email_run
from modules.ai.schedule_conflict_detector import run as conflict_run

ROLE_TOOLS = {
    "admin": {
        "📋 Training Plan Optimizer": training_run,
        "⚠️ Conflict Detector": conflict_run,
        "🏀 Demand Predictor": demand_run,
        "📬 Email Predictor": email_run,
        "🎓 Scholarship AI": scholarship_run
    },
    "coach": {
        "📋 Training Plan Optimizer": training_run,
        "⚠️ Conflict Detector": conflict_run
    },
    "marketing": {
        "📬 Email Predictor": email_run
    },
    "foundation": {
        "🎓 Scholarship AI": scholarship_run,
        "🎯 Youth Tracker": youth_run
    },
    "sponsor": {
        "🤝 Event Sponsorship Matcher": sponsorship_run
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
    st.set_page_config(page_title="SportAI Ultra Dashboard", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    st.title("SportAI Ultra: Role-Based AI Tools")
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools available for this role.")
        return
    selection = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if selection:
        tools[selection]()

run()
