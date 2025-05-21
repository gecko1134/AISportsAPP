
import streamlit as st
import json
from modules.ai.revenue_projection_ai import run as revenue_run
from modules.ai.surface_demand_heatmap import run as heatmap_run
from modules.ai.grant_scoring_ai import run as grant_run
from modules.ai.sponsor_impact_predictor import run as sponsor_impact_run
from modules.ai.event_forecaster import run as event_forecast_run
from modules.ai.financial_risk_ai import run as risk_run
from modules.ai.member_segmentation_ai import run as segment_run
from modules.ai.donor_retention_predictor import run as retention_run
from modules.ai.facility_efficiency_ai import run as efficiency_run
from modules.ai.budget_optimizer_ai import run as budget_run
from modules.ai.credit_forecast_ai import run as credit_run

ROLE_TOOLS = {
    "admin": {
        "📊 Revenue Projection": revenue_run,
        "📈 Heatmap": heatmap_run,
        "💸 Risk Detection": risk_run,
        "🧩 Segmentation": segment_run,
        "📊 Budget Optimizer": budget_run
    },
    "board": {
        "📊 Revenue Projection": revenue_run,
        "💸 Risk Detection": risk_run,
        "📊 Budget Optimizer": budget_run
    },
    "sponsor": {
        "💡 Impact Prediction": sponsor_impact_run
    },
    "foundation": {
        "🎯 Grant Scoring": grant_run,
        "🔁 Donor Retention": retention_run
    },
    "donor": {
        "🔁 Donor Retention": retention_run
    },
    "member": {
        "🧩 Segmentation": segment_run,
        "💳 Credit Forecast": credit_run
    },
    "tournament_director": {
        "📅 Event Forecasting": event_forecast_run
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
    st.set_page_config(page_title="SportAI Role-Based Dashboard", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    role = st.session_state.user["role"]
    st.sidebar.success(f"Logged in as {st.session_state.user['email']} ({role})")
    logout()
    st.title("SportAI: AI Dashboard by Role")
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools assigned to this role.")
        return
    choice = st.sidebar.selectbox("Choose a Tool", list(tools.keys()))
    if choice:
        tools[choice]()

run()
