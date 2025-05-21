
import streamlit as st
import pandas as pd
from modules.ai.revenue_projection_ai import run as revenue_run
from modules.ai.surface_demand_heatmap import run as heatmap_run
from modules.ai.grant_scoring_ai import run as grant_run
from modules.ai.sponsor_impact_predictor import run as sponsor_impact_run
from modules.ai.event_forecaster import run as event_forecast_run
from modules.ai.financial_risk_ai import run as risk_run

TOOLS = {
    "📊 Revenue Projection AI": revenue_run,
    "📈 Surface Demand Heatmap": heatmap_run,
    "🎯 Grant Scoring AI": grant_run,
    "💡 Sponsor Impact Predictor": sponsor_impact_run,
    "📅 Event Forecaster": event_forecast_run,
    "💸 Financial Risk AI": risk_run
}

st.set_page_config(page_title='SportAI Suite', layout='wide')
st.title("SportAI Suite – Real-Time AI Tools")

tool = st.sidebar.selectbox("Select an AI Tool", list(TOOLS.keys()))
if tool:
    TOOLS[tool]()
