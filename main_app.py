import os, sys
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
import json

from modules.ai.demand_forecasting import DemandForecaster
from modules.scheduling.optimizer import optimize_schedule
from modules.sponsorship.matcher import match_sponsors
from modules.sponsorship.contract_generator import generate_contract
from modules.ai.churn_prediction import ChurnPredictor
from modules.marketing.campaign_optimizer import optimize_campaign

with open(os.path.join(BASE_DIR, 'users.json')) as f:
    users = json.load(f)

def login():
    st.sidebar.header('🔐 Login')
    email = st.sidebar.text_input('Email')
    password = st.sidebar.text_input('Password', type='password')
    if st.sidebar.button('Login'):
        user = users.get(email)
        if user and user['password'] == password:
            st.session_state.user = {'email': email, 'role': user['role']}
        else:
            st.sidebar.error('Invalid credentials.')

def logout():
    if st.sidebar.button('Logout'):
        st.session_state.user = None

def demand_forecasting_ui():
    st.header("📈 Demand Forecasting")
    file = st.file_uploader("Upload booking history CSV", type="csv", key="forecast")
    if file:
        import pandas as pd
        df = pd.read_csv(file)
        feature_cols = st.multiselect("Select feature columns", df.columns.tolist())
        target_col = st.selectbox("Select target column", df.columns.tolist())
        if st.button("Train + Predict"):
            model = DemandForecaster()
            model.train(df, feature_cols, target_col)
            preds = model.predict(df[feature_cols])
            st.write(preds)

def schedule_optimizer_ui():
    st.header("📅 Schedule Optimizer")
    req_file = st.file_uploader("Upload requests CSV", type="csv", key="requests")
    if req_file:
        import pandas as pd
        df = pd.read_csv(req_file).set_index("id")
        time_slots = st.text_input("Enter time slots (comma-separated)", "t1,t2,t3").split(",")
        resources = {slot: st.number_input(f"Resources for {slot}", 1, 100, 10) for slot in time_slots}
        if st.button("Run Optimization"):
            result = optimize_schedule(df, resources, time_slots)
            st.write(result)

def sponsor_match_ui():
    st.header("🤝 Sponsorship Matcher")
    a_file = st.file_uploader("Upload assets CSV", type="csv", key="assets")
    s_file = st.file_uploader("Upload sponsors CSV", type="csv", key="sponsors")
    if a_file and s_file:
        import pandas as pd
        assets = pd.read_csv(a_file)
        sponsors = pd.read_csv(s_file)
        matched = match_sponsors(assets, sponsors)
        st.write(matched)

def contract_generator_ui():
    st.header("📄 Generate Contract")
    template_id = st.text_input("Template ID")
    api_key = st.text_input("PandaDoc API Key", type="password")
    name = st.text_input("Recipient Name")
    email = st.text_input("Recipient Email")
    amount = st.number_input("Contract Value", 100, 1000000, 1000)
    if st.button("Generate"):
        data = {"name": name, "email": email, "cost": amount}
        result = generate_contract(template_id, data, api_key)
        st.write(result)

def churn_prediction_ui():
    st.header("🚨 Churn Prediction")
    churn_file = st.file_uploader("Upload member data CSV", type="csv", key="churn")
    if churn_file:
        import pandas as pd
        df = pd.read_csv(churn_file)
        features = st.multiselect("Select feature columns", df.columns.tolist())
        if st.button("Predict Churn"):
            model = ChurnPredictor()
            model.train(df, features, "churn")
            probs = model.predict(df[features])
            st.write(probs)

def campaign_optimizer_ui():
    st.header("📣 Marketing Campaign Optimizer")
    invites_file = st.file_uploader("Upload invites A/B CSV", type="csv", key="campaign")
    if invites_file:
        import pandas as pd
        df = pd.read_csv(invites_file)
        result = optimize_campaign(df)
        st.write(result)

ROLE_TOOLS = {
    "admin": {
        "Demand Forecasting": demand_forecasting_ui,
        "Schedule Optimizer": schedule_optimizer_ui,
        "Sponsorship Matcher": sponsor_match_ui,
        "Contract Generator": contract_generator_ui,
        "Churn Prediction": churn_prediction_ui,
        "Campaign Optimization": campaign_optimizer_ui
    },
    "sponsor": {
        "Sponsorship Matcher": sponsor_match_ui,
        "Contract Generator": contract_generator_ui,
        "Campaign Optimization": campaign_optimizer_ui
    },
    "member": {
        "Demand Forecasting": demand_forecasting_ui,
        "Schedule Optimizer": schedule_optimizer_ui
    },
    "board": {
        "Demand Forecasting": demand_forecasting_ui,
        "Churn Prediction": churn_prediction_ui
    },
    "foundation": {
        "Campaign Optimization": campaign_optimizer_ui
    }
}

def run():
    st.set_page_config(page_title='SportAI Suite', layout='wide')
    if 'user' not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user['role']
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    st.title('SportAI Suite – Interactive Tools')
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools assigned to your role.")
        return
    selection = st.sidebar.selectbox('Available Tools', list(tools.keys()))
    if selection in tools:
        tools[selection]()

run()
