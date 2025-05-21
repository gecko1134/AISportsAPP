
import streamlit as st
import json
import importlib

CATEGORIES = {
    "🧠 Player Performance": {
        "💪 Strength Tracker": "modules.performance.strength_tracker",
        "⚡ Speed Analyzer": "modules.performance.speed_analyzer",
        "🤸 Agility Visualizer": "modules.performance.agility_visualizer"
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
    st.set_page_config(page_title="SportAI Subdomain Suite", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    logout()
    st.sidebar.success(f"Logged in as {st.session_state.user['email']} ({st.session_state.user['role']})")
    category = st.sidebar.selectbox("Select Category", list(CATEGORIES.keys()))
    tools = CATEGORIES[category]
    label = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if label:
        try:
            mod = importlib.import_module(tools[label])
            mod.run()
        except Exception as e:
            st.error(f"Error loading tool: {e}")

run()
