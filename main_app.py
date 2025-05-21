
import streamlit as st
import json
import importlib

ROLE_TOOLS = {
    "admin": {
        "🛠️ Incident Reports": "modules.new.incident_report_logger",
        "🗂️ Contract Compiler": "modules.new.contract_compiler",
        "💬 Messaging AI": "modules.new.internal_messaging_ai"
    },
    "coach": {
        "🏆 Athlete Development": "modules.new.athlete_development_tracker"
    },
    "education": {
        "🎓 Workshop Scheduler": "modules.new.workshop_scheduler"
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
    st.set_page_config(page_title="SportAI GitHub Ready", layout="wide")
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
    label = st.sidebar.selectbox("Choose a Tool", list(tools.keys()))
    if label:
        try:
            mod = importlib.import_module(tools[label])
            mod.run()
        except Exception as e:
            st.error(f"Failed to load: {e}")

run()
