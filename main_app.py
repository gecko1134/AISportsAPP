import os, sys
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
import json

from ai_modules.demand_forecasting import DemandForecaster
from ai_modules.scheduling_optimizer import optimize_schedule
from ai_modules.sponsorship_matcher import match_sponsors
from ai_modules.dynamic_contract_generator import generate_contract
from ai_modules.membership_churn import ChurnPredictor
from ai_modules.marketing_optimizer import optimize_campaign

with open('users.json') as f:
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

TOOLS = {
    "Demand Forecasting": DemandForecaster,
    "Schedule Optimizer": optimize_schedule,
    "Sponsorship Matcher": match_sponsors,
}

def run():
    st.set_page_config(page_title='Venture North Admin', layout='wide')
    if 'user' not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    st.sidebar.success(f"Logged in as {user['email']} ({user['role']})")
    logout()
    st.title('SportAI Suite with AI Modules')
    st.sidebar.title('AI Optimizations')
    if st.sidebar.button('Forecast Demand'):
        st.write('Demand Forecast placeholder')
    if st.sidebar.button('Optimize Schedule'):
        st.write('Optimized Schedule placeholder')
    if st.sidebar.button('Match Sponsors'):
        st.write('Sponsor Matches placeholder')

run()
