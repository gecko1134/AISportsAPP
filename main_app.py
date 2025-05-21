
import streamlit as st
import json
import importlib

CATEGORIES = {
    "📊 Analytics": {
        "📜 Donor History Analyzer": "modules.ai.donor_history_analyzer",
        "📈 Player Development Scorecard": "modules.ai.player_dev_scorecard"
    },
    "💼 Finance": {
        "💰 Budget Planner AI": "modules.ai.budget_planner"
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
    st.set_page_config(page_title="SportAI Categories", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    logout()
    st.sidebar.success(f"Logged in as {st.session_state.user['email']} ({st.session_state.user['role']})")
    category = st.sidebar.selectbox("Select Category", list(CATEGORIES.keys()))
    tools = CATEGORIES[category]
    tool_label = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    module_path = tools[tool_label]
    try:
        mod = importlib.import_module(module_path)
        mod.run()
    except Exception as e:
        st.error(f"Error loading {tool_label}: {e}")

run()
