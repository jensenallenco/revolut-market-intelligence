import streamlit as st
import pandas as pd

from plots.sector_analysis import render_sector_chart
from plots.age_analysis import render_age_chart
from plots.kpi_metrics import calculate_top_metrics

st.set_page_config(page_title="Revolut Executive Intelligence", layout="wide")

# Inject minimal global custom styling to force clean dark card parameters
st.markdown("""
    <style>
        .stApp { background-color: #0b0d17; color: #ffffff; }
        div[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 700 !important; color: #ffffff; }
        div[data-testid="stMetricLabel"] { color: #848e9c !important; font-size: 0.85rem !important; text-transform: uppercase; letter-spacing: 0.5px; }
        hr { border-color: #1c2236 !important; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_and_preprocess_data():
    df_sec = pd.read_excel("revolut_dataset_may2026.xlsx", sheet_name="1.Spending by Sector NSA", skiprows=4)
    df_a = pd.read_excel("revolut_dataset_may2026.xlsx", sheet_name="2.Spending by Age NSA", skiprows=4)
    
    df_sec['Date'] = pd.to_datetime(df_sec['Date'], errors='coerce')
    df_a['Date'] = pd.to_datetime(df_a['Date'], errors='coerce')
    
    return df_sec.dropna(subset=['Date']), df_a.dropna(subset=['Date'])

df_sector, df_age = load_and_preprocess_data()
metrics = calculate_top_metrics(df_sector, df_age)

# --- HEADER SECTION ---
st.title("Revolut Market Intelligence Engine")
st.markdown("*Modular Analytics Architecture Layer | ONS Macro Consumer Transaction Data (UK)*")
st.markdown("---")

# --- EXECUTIVE LAYER: KPI SUMMARY MARGINS ---
st.markdown("### Platform Performance Aggregates")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.metric(label="Platform Spend Index", value=metrics["latest_total"], delta=metrics["total_delta"])
with kpi_col2:
    st.metric(label="Dominant Consumer Vertical", value=metrics["peak_sector"], delta="Top Active Category")
with kpi_col3:
    st.metric(label="Mature Market Multiplier", value=metrics["demographic_ratio"], delta="Velocity Ratio (55+ / 18-34)")

st.markdown("---")

# --- OPERATIONAL LAYER: DATA MATRIX SPLIT ---
st.markdown("### Core Operational Trends")
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("#### Sector Velocity Funnel")
    available_sectors = [col for col in df_sector.columns if col not in ['Date', 'Total']]
    selected_sectors = st.multiselect("Filter Analysis Verticals:", available_sectors, default=["Travel", "Entertainment", "Groceries"])
    
    fig_sector = render_sector_chart(df_sector, selected_sectors)
    st.pyplot(fig_sector)

with right_col:
    st.markdown("#### Demographic Trajectory Split")
    available_ages = ["18-34", "35-54", "55+"]
    selected_ages = st.multiselect("Filter Targeted Customer Demographics:", available_ages, default=["18-34", "35-54", "55+"])
    
    fig_age = render_age_chart(df_age, selected_ages)
    st.pyplot(fig_age)

st.markdown("---")
st.caption("Internal telemetry tracking model prepared for product and data science alignment protocols.")