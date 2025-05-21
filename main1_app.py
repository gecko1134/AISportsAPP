
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
import streamlit as st
import json
import importlib

CATEGORIES = {
    "📈 Reporting & Exports": {
        "📄 PDF Report Generator": "modules.reporting.pdf_report_generator",
        "📊 Budget Visualizer": "modules.reporting.budget_visualizer"
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
    st.set_page_config(page_title="SportAI Cloud Suite", layout="wide")
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
import streamlit as st
import json
import importlib

ROLE_TOOLS = {
    "admin": {
        "🩺 Injury Log": "modules.ops.injury_log_ai",
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner"
    },
    "referee": {
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner"
    },
    "medical_staff": {
        "🩺 Injury Log": "modules.ops.injury_log_ai"
    }
}

def login():
    st.sidebar.header("🔐 Login")
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
    st.set_page_config(page_title="SportAI Final Dashboard", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools available for this role.")
        return
    label = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if label:
        try:
            mod = importlib.import_module(tools[label])
            mod.run()
        except Exception as e:
            st.error(f"Tool failed: {e}")

run()
import streamlit as st
import json
import importlib

ROLE_TOOLS = {
    "admin": {
        "🩺 Injury Log": "modules.ops.injury_log_ai",
        "🙋 Waiver Tracker": "modules.ops.volunteer_waiver_tracker",
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner",
        "📅 Trainer Scheduler": "modules.ops.trainer_schedule_ai",
        "📋 Game Checklist": "modules.ops.game_day_checklist"
    },
    "referee": {
        "🧑‍⚖️ Referee Assigner": "modules.ops.referee_assigner"
    },
    "medical_staff": {
        "🩺 Injury Log": "modules.ops.injury_log_ai",
        "📅 Trainer Scheduler": "modules.ops.trainer_schedule_ai"
    },
    "volunteer": {
        "🙋 Waiver Tracker": "modules.ops.volunteer_waiver_tracker"
    },
    "scheduler_admin": {
        "📋 Game Checklist": "modules.ops.game_day_checklist"
    },
    "event_ops": {
        "📋 Game Checklist": "modules.ops.game_day_checklist"
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
    st.set_page_config(page_title="SportAI Ops Dashboard", layout="wide")
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
    selection = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if selection:
        try:
            mod = importlib.import_module(tools[selection])
            mod.run()
        except Exception as e:
            st.error(f"Tool failed to run: {e}")

run()
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
import streamlit as st
import json
from modules.ai.training_plan_optimizer import run as training_run
from modules.ai.event_sponsorship_matcher import run as sponsorship_run
from modules.ai.multi_sport_demand_predictor import run as demand_run
from modules.ai.youth_engagement_tracker import run as youth_run
from modules.ai.scholarship_probability_ai import run as scholarship_run
from modules.ai.email_response_predictor import run as email_run
from modules.ai.schedule_conflict_detector import run as conflict_run

ROLE_TOOLS = {
    "admin": {
        "📋 Training Plan Optimizer": training_run,
        "⚠️ Conflict Detector": conflict_run,
        "🏀 Demand Predictor": demand_run,
        "📬 Email Predictor": email_run,
        "🎓 Scholarship AI": scholarship_run
    },
    "coach": {
        "📋 Training Plan Optimizer": training_run,
        "⚠️ Conflict Detector": conflict_run
    },
    "marketing": {
        "📬 Email Predictor": email_run
    },
    "foundation": {
        "🎓 Scholarship AI": scholarship_run,
        "🎯 Youth Tracker": youth_run
    },
    "sponsor": {
        "🤝 Event Sponsorship Matcher": sponsorship_run
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
    st.set_page_config(page_title="SportAI Ultra Dashboard", layout="wide")
    if "user" not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()
    st.title("SportAI Ultra: Role-Based AI Tools")
    tools = ROLE_TOOLS.get(role, {})
    if not tools:
        st.warning("No tools available for this role.")
        return
    selection = st.sidebar.selectbox("Select Tool", list(tools.keys()))
    if selection:
        tools[selection]()

run()
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

run()import streamlit as st
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


import os
import sys

BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from ai_modules.demand_forecasting import DemandForecaster
from ai_modules.scheduling_optimizer import optimize_schedule
from ai_modules.sponsorship_matcher import match_sponsors
from ai_modules.dynamic_contract_generator import generate_contract
from ai_modules.membership_churn import ChurnPredictor
from ai_modules.marketing_optimizer import optimize_campaign


import optimize_schedule
import match_sponsors
import generate_contract
import ChurnPredictor
import optimize_campaign
import member_selector
import auto_contract_generator
import header_loader
import fundraising_launch_center
import grant_renewal_manager
import investor_kit_generator
import board_packet_pdf_generator
import funding_narrative_sync
import crm_pipeline_dashboard
import board_report_scheduler
import hubspot_deal_logger
import sponsor_pitch_portal
import mailchimp_lead_collector
import marketing_packet_builder
import screen_rotation_scheduler
import media_display_rotator
import investor_pitch_portal
import admin_override_console
import expiring_link_manager
import sponsor_link_sender
import flipbook_pitch_creator
import sponsor_pdf_packet
import sponsor_pitchbook_builder
import sponsor_proposal_pdf
import ai_sponsor_pricing_trends
import sponsorship_inventory_limiter
import crm_grant_donor_sync
import pdf_grant_exporter
import grant_alert_center
import grant_writer_ai
import grant_match_ai
import grant_status_manager
import donation_landing_page
import crm_export_generator
import donation_checkout
import donation_campaign_viewer
import donor_match_ai
import donor_message_builder
import donor_profile_creator
import donation_goal_tracker
import portal_router
import upsell_offer_engine
import member_portal
import sponsor_portal
import public_schedule
import sponsor_map_viewer
import ai_facility_chat
import slack_alert_center
import webhook_automation
import admin_sidebar_badges
import daily_task_scheduler
import ai_voice_responder
import member_alerts_auto
import credential_expiry_alerts
import usage_alerts_auto
import contract_alerts_auto
import platform_guidebook_writer
import board_pdf_exporter
import finance_feed_connector
import board_financial_summary
import revenue_projection_simulator
import sponsorship_revenue_builder
import event_admin
import surface_usage_by_type
import governance_admin
import governance_diagram
import financial_feed_sync
import sms_alert_center
import real_time_dashboard
import gsheets_sync
import event_profit_analyzer
import adaptive_use_planner
import park_activity_dashboard
import surface_demand_heatmap
import tournament_scheduler
import international_team_portal
import esports_manager
import adaptive_sports_center
import streamlit as st
import json
import auth
import ai_event_forecast
import ai_matchmaker_tool
import ai_revenue_maximizer
import ai_scheduler_tool
import ai_scheduling_suggestions
import ai_sponsor_opportunity_finder
import ai_strategy_dashboard
import ai_suggestion_digest
import ai_voice_command
import auth
import central_dashboard
import complex_usage_optimizer
import contract_insights_ai
import contract_usage_tracker
import dome_usage_tool
import dynamic_pricing_tool
import email_notifications
import event_control_panel
import event_creator_ai
import event_types_config
import facility_access_tracker
import facility_capacity_alerts
import facility_contract_monitor
import facility_layout_map
import facility_master_tracker
import facility_membership_comparator_ai
import facility_membership_monitor
import flipbook_embedder
import google_sheets_sync
import governance_tool
import league_coordinator
import marketing_flipbook_generator
import membership_credit_tracker
import membership_crm_tracker
import membership_dashboard
import membership_goal_tracker
import membership_insights_ai
import membership_loyalty_rewards
import membership_marketing_ai
import membership_ticketing_integration
import mentorship_center
import mobile_friendly_ui
import nil_tracker
import pandadoc_contract
import pdf_export_tool
import performance_goal_ai
import proposal_to_pdf
import referee_manager
import report_download_portal
import revenue_heatmap
import revenue_proforma_auto
import scholarship_fund_manager
import scholarship_tracker
import setup_assistant_ai
import sponsor_dashboard
import sponsorship_ai_calculator
import sponsorship_availability
import sponsorship_contract_generator
import sponsorship_inventory_manager
import sponsorship_roi_tracker
import sponsorship_tracker
import sport_library
import student_committee
import team_club_manager
import trail_access_planner
import visual_calendar_layout
import volunteer_hub
import weekly_report_generator
import investor_pitch_portal
import admin_override_console




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
    "Ai Event Forecast": ai_event_forecast,
    "Ai Matchmaker Tool": ai_matchmaker_tool,
    "Ai Revenue Maximizer": ai_revenue_maximizer,
    "Ai Scheduler Tool": ai_scheduler_tool,
    "Ai Scheduling Suggestions": ai_scheduling_suggestions,
    "Ai Sponsor Opportunity Finder": ai_sponsor_opportunity_finder,
    "Ai Strategy Dashboard": ai_strategy_dashboard,
    "Ai Suggestion Digest": ai_suggestion_digest,
    "Ai Voice Command": ai_voice_command,
    "Auth": auth,
    "Central Dashboard": central_dashboard,
    "Complex Usage Optimizer": complex_usage_optimizer,
    "Contract Insights Ai": contract_insights_ai,
    "Contract Usage Tracker": contract_usage_tracker,
    "Dome Usage Tool": dome_usage_tool,
    "Dynamic Pricing Tool": dynamic_pricing_tool,
    "Email Notifications": email_notifications,
    "Event Control Panel": event_control_panel,
    "Event Creator Ai": event_creator_ai,
    "Event Types Config": event_types_config,
    "Facility Access Tracker": facility_access_tracker,
    "Facility Capacity Alerts": facility_capacity_alerts,
    "Facility Contract Monitor": facility_contract_monitor,
    "Facility Layout Map": facility_layout_map,
    "Facility Master Tracker": facility_master_tracker,
    "Facility Membership Comparator Ai": facility_membership_comparator_ai,
    "Facility Membership Monitor": facility_membership_monitor,
    "Flipbook Embedder": flipbook_embedder,
    "Google Sheets Sync": google_sheets_sync,
    "Governance Tool": governance_tool,
    "League Coordinator": league_coordinator,
    "Marketing Flipbook Generator": marketing_flipbook_generator,
    "Membership Credit Tracker": membership_credit_tracker,
    "Membership Crm Tracker": membership_crm_tracker,
    "Membership Dashboard": membership_dashboard,
    "Membership Goal Tracker": membership_goal_tracker,
    "Membership Insights Ai": membership_insights_ai,
    "Membership Loyalty Rewards": membership_loyalty_rewards,
    "Membership Marketing Ai": membership_marketing_ai,
    "Membership Ticketing Integration": membership_ticketing_integration,
    "Mentorship Center": mentorship_center,
    "Mobile Friendly Ui": mobile_friendly_ui,
    "Nil Tracker": nil_tracker,
    "Pandadoc Contract": pandadoc_contract,
    "Pdf Export Tool": pdf_export_tool,
    "Performance Goal Ai": performance_goal_ai,
    "Proposal To Pdf": proposal_to_pdf,
    "Referee Manager": referee_manager,
    "Report Download Portal": report_download_portal,
    "Revenue Heatmap": revenue_heatmap,
    "Revenue Proforma Auto": revenue_proforma_auto,
    "Scholarship Fund Manager": scholarship_fund_manager,
    "Scholarship Tracker": scholarship_tracker,
    "Setup Assistant Ai": setup_assistant_ai,
    "Sponsor Dashboard": sponsor_dashboard,
    "Sponsorship Ai Calculator": sponsorship_ai_calculator,
    "Sponsorship Availability": sponsorship_availability,
    "Sponsorship Contract Generator": sponsorship_contract_generator,
    "Sponsorship Inventory Manager": sponsorship_inventory_manager,
    "Sponsorship Roi Tracker": sponsorship_roi_tracker,
    "Sponsorship Tracker": sponsorship_tracker,
    "Sport Library": sport_library,
    "Student Committee": student_committee,
    "Team Club Manager": team_club_manager,
    "Trail Access Planner": trail_access_planner,
    "Visual Calendar Layout": visual_calendar_layout,
    "Volunteer Hub": volunteer_hub,
    "Weekly Report Generator": weekly_report_generator,
    "Esports Manager": esports_manager,
    "Adaptive Sports Center": adaptive_sports_center,
    "Tournament Scheduler": tournament_scheduler,
    "International Team Portal": international_team_portal,
    "Park Activity Dashboard": park_activity_dashboard,
    "Surface Demand Heatmap": surface_demand_heatmap,
    "Event Profitability Analyzer": event_profit_analyzer,
    "Adaptive Use Planner": adaptive_use_planner,
    "Real-Time Dashboard": real_time_dashboard,
    "Google Sheets Sync": gsheets_sync,
    "SMS Alert Center": sms_alert_center,
    "Event Admin": event_admin,
    "Surface Usage by Type": surface_usage_by_type,
    "Governance Admin": governance_admin,
    "Governance Diagram": governance_diagram,
    "Financial Feed Sync": financial_feed_sync,
    "Revenue Projection Simulator": revenue_projection_simulator,
    "Sponsorship Revenue Builder": sponsorship_revenue_builder,
    "Board Financial Summary": board_financial_summary,
    "Board PDF Exporter": board_pdf_exporter,
    "Finance Feed Connector": finance_feed_connector,
    "Platform Guidebook": platform_guidebook_writer,
    "Surface Gap Alerts": usage_alerts_auto,
    "Sponsor Contract Alerts": contract_alerts_auto,
    "Member Alerts Auto": member_alerts_auto,
    "Credential Expiry Alerts": credential_expiry_alerts,
    "Daily Task Scheduler": daily_task_scheduler,
    "Voice Assistant": ai_voice_responder,
    "Admin Sidebar Badges": admin_sidebar_badges,
    "Slack Alert Center": slack_alert_center,
    "Webhook Automation": webhook_automation,
    "AI Facility Chat": ai_facility_chat,
    "Public Schedule": public_schedule,
    "Sponsor Map Viewer": sponsor_map_viewer,
    "Member Portal": member_portal,
    "Sponsor Portal": sponsor_portal,
    "Portal Router": portal_router,
    "Upsell Offer Engine": upsell_offer_engine,
    "Donor Profile Creator": donor_profile_creator,
    "Donation Goal Tracker": donation_goal_tracker,
    "Donor Match AI": donor_match_ai,
    "Donor Message Builder": donor_message_builder,
    "Donation Checkout": donation_checkout,
    "Donation Campaign Viewer": donation_campaign_viewer,
    "Public Donation Page": donation_landing_page,
    "CRM Export Builder": crm_export_generator,
    "AI Grant Match": grant_match_ai,
    "Grant Status Tracker": grant_status_manager,
    "Grant Alerts": grant_alert_center,
    "AI Grant Writer": grant_writer_ai,
    "CRM Sync (Grants & Donors)": crm_grant_donor_sync,
    "PDF Grant Exporter": pdf_grant_exporter,
    "AI Sponsor Pricing Trends": ai_sponsor_pricing_trends,
    "Sponsor Inventory Limits": sponsorship_inventory_limiter,
    "AI Sponsorship Pitchbook": sponsor_pitchbook_builder,
    "Sponsor Proposal PDF": sponsor_proposal_pdf,
    "Flipbook Pitch Creator": flipbook_pitch_creator,
    "Sponsor Packet PDF": sponsor_pdf_packet,
    "Sponsor Link Generator": sponsor_link_generator,
    "Expiring Link Generator": expiring_link_manager,
    "Sponsor Link Sender": sponsor_link_sender,
    "Investor Portal": investor_pitch_portal,
    "Admin Override Console": admin_override_console,
    "Investor Portal": investor_pitch_portal,
    "Admin Override Console": admin_override_console,
    "Screen Scheduler": screen_rotation_scheduler,
    "Media Rotator": media_display_rotator,
    "Marketing Packet Builder": marketing_packet_builder,
    "Sponsor Pitch Portal": sponsor_pitch_portal,
    "Mailchimp Lead Collector": mailchimp_lead_collector,
    "HubSpot Deal Logger": hubspot_deal_logger,
    "CRM Pipeline Dashboard": crm_pipeline_dashboard,
    "Board Report Scheduler": board_report_scheduler,
    "Board Packet Generator": board_packet_pdf_generator,
    "Fundraising Narrative Sync": funding_narrative_sync,
    "Grant Renewal Tracker": grant_renewal_manager,
    "Investor Kit Generator": investor_kit_generator,
    "Fundraising Launch Center": fundraising_launch_center,
    "Membership Recommender": member_selector,
    "Contract Generator": auto_contract_generator,
}

def run():
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
    st.set_page_config(page_title='Venture North Admin', layout='wide')
    if 'user' not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    st.sidebar.success(f"Logged in as {user['email']} ({user['role']})")
    logout()
    selection = st.sidebar.selectbox('Choose a Tool', list(TOOLS.keys()))
    if selection in TOOLS:
        TOOLS[selection].run()
        header_loader.run()
        st.sidebar.title('AI Optimizations')

if st.sidebar.button('Forecast Demand'):
    st.write('Demand Forecast:')
    # TODO: load booking_data.csv and call DemandForecaster.predict()

if st.sidebar.button('Optimize Schedule'):
    st.write('Optimized Schedule:')
    # TODO: load schedule_requests.csv, resources.json, call optimize_schedule()

if st.sidebar.button('Match Sponsors'):
    st.write('Sponsor Matches:')
    # TODO: load assets.csv and sponsors.csv, call match_sponsors()

if st.sidebar.button('Generate Dynamic Contract'):
    st.write('Contract Link:')
    # TODO: call generate_contract(template_id, data, api_key) and show URL

if st.sidebar.button('Predict Churn'):
    st.write('Churn Risk Scores:')
    # TODO: load member_features.csv, call ChurnPredictor.predict()

if st.sidebar.button('Optimize Campaign'):
    st.write('Campaign Result:')
    # TODO: load invites.csv, call optimize_campaign()

st.title('SportAI Suite with AI Modules')
st.write('Select an AI tool from the sidebar to get started.')

run()
