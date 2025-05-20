import os, sys
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
from ai_modules.demand_forecasting import DemandForecaster
from ai_modules.scheduling_optimizer import optimize_schedule
from ai_modules.sponsorship_matcher import match_sponsors
from ai_modules.dynamic_contract_generator import generate_contract
from ai_modules.membership_churn import ChurnPredictor
from ai_modules.marketing_optimizer import optimize_campaign

st.title("AI Tools Test")
st.write("All modules imported successfully.")
