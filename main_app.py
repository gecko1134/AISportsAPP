
import streamlit as st
import json
import importlib

ROLE_TOOLS = {
    "admin": {
        "📊 Revenue Projection": "modules.ai.revenue_projection_ai",
        "🎯 Grant Scoring": "modules.ai.grant_scoring_ai",
        "📅 Event Forecasting": "modules.ai.event_forecaster"
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
    st.set_page_config(page_title="SportAI Cloud", layout="wide")
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
    choice = st.sidebar.selectbox("Choose a Tool", list(tools.keys()))
    if choice:
        try:
            mod = importlib.import_module(tools[choice])
            mod.run()
        except Exception as e:
            st.error(f"Error loading tool: {e}")

run()
