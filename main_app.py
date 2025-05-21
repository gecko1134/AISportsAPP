
import streamlit as st
import json
import os
import importlib

# Load users
def load_users():
    with open("users.json") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)

def login():
    st.sidebar.header("🔐 Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        users = load_users()
        user = users.get(email)
        if user and user["password"] == password:
            st.session_state.user = {"email": email, "role": user["role"]}
        else:
            st.sidebar.error("Invalid credentials.")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.user = None

# Tool categories
CATEGORIES = {
    "📊 Analytics": ["modules.ai.youth_engagement_tracker", "modules.ai.email_response_predictor"],
    "📅 Scheduling": ["modules.ai.schedule_conflict_detector", "modules.ai.training_plan_optimizer"],
    "🧠 AI Forecasting": ["modules.ai.multi_sport_demand_predictor", "modules.ai.event_forecaster"],
    "💼 Financial Tools": ["modules.ai.revenue_projection_ai", "modules.ai.budget_optimizer_ai"],
    "👥 Governance": ["modules.ai.scholarship_probability_ai", "modules.ai.grant_scoring_ai"]
}

# Flatten category dictionary
ALL_TOOLS = {tool: mod for cat in CATEGORIES.values() for mod in cat for tool in [mod.split('.')[-1].replace('_', ' ').title()]}

def run_admin_panel():
    st.subheader("👤 User Management (Admin Only)")
    users = load_users()
    st.write("### Current Users")
    st.json(users)
    st.write("### Add New User")
    new_email = st.text_input("New Email")
    new_pass = st.text_input("New Password", type="password")
    new_role = st.selectbox("Role", ["admin", "coach", "marketing", "foundation", "sponsor", "member", "board"])
    if st.button("Add User"):
        if new_email and new_pass:
            users[new_email] = {"password": new_pass, "role": new_role}
            save_users(users)
            st.success(f"User {new_email} added.")
        else:
            st.error("Missing email or password.")

def run():
    st.set_page_config(page_title="SportAI Enhanced", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    st.title("SportAI Enhanced: AI Tools by Category")
    if role == "admin":
        run_admin_panel()
    category = st.sidebar.selectbox("Tool Category", list(CATEGORIES.keys()))
    tool_module_paths = CATEGORIES[category]
    tool_labels = [mod.split('.')[-1].replace('_', ' ').title() for mod in tool_module_paths]
    selected_label = st.sidebar.selectbox("Select Tool", tool_labels)
    selected_module = tool_module_paths[tool_labels.index(selected_label)]
    try:
        mod = importlib.import_module(selected_module)
        mod.run()
    except Exception as e:
        st.error(f"❌ Error loading tool: {e}")

run()
