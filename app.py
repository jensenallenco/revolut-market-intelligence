import streamlit as st
import pandas as pd

# Dynamic modular imports
from plots.sector_analysis import render_sector_chart, get_sector_insights
from plots.age_analysis import render_age_chart, get_age_insights
from plots.kpi_metrics import calculate_top_metrics

st.set_page_config(page_title="Revolut Debit Card Spending Indicators — UK", layout="wide")

# Global clean styling overrides
st.markdown("""
    <style>
        .stApp { background-color: #0b0d17; color: #ffffff; }
        div[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 700 !important; color: #ffffff; }
        div[data-testid="stMetricLabel"] { color: #848e9c !important; font-size: 0.85rem !important; letter-spacing: 0.5px; }
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
st.title("Revolut Debit Card Spending Indicators — UK")
st.markdown("*Weekly and monthly consumer spending index trends based on Revolut debit card transactions*")
st.markdown("Official statistics in development from the ONS Real Time Indicators dataset")
st.markdown("---")

# --- KPI SECTION: SPENDING INDEX SUMMARY ---
st.markdown("### Spending Index Summary")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.metric(label="Latest Spending Index", value=metrics["latest_total"], delta=metrics["total_delta"])
with kpi_col2:
    st.metric(label="Top Spending Category", value=metrics["top_spending_cat"], delta="Highest Relative Volume")
with kpi_col3:
    st.metric(label="55+ vs 18–34 Spending Ratio", value=metrics["spending_ratio"], delta="Older vs Younger Cohort Index")

st.markdown("---")

# --- CHARTS & INSIGHTS SECTION: SPENDING TRENDS OVER TIME ---
st.markdown("### Spending Trends Over Time")
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("#### Spending by Category")
    available_sectors = [col for col in df_sector.columns if col not in ['Date', 'Total']]
    selected_sectors = st.multiselect("Filter Spending Categories:", available_sectors, default=["Travel", "Entertainment", "Groceries"])
    
    fig_sector = render_sector_chart(df_sector, selected_sectors)
    st.pyplot(fig_sector)
    
    # Dataset-faithful Category Observation Card
    with st.container(border=True):
        st.markdown("**Statistical Summary — Category Selection**")
        st.write(get_sector_insights(df_sector, selected_sectors))

with right_col:
    st.markdown("#### Spending by Age Group")
    available_ages = ["18-34", "35-54", "55+"]
    selected_ages = st.multiselect("Filter Age Groups:", available_ages, default=["18-34", "35-54", "55+"])
    
    fig_age = render_age_chart(df_age, selected_ages)
    st.pyplot(fig_age)
    
    # Dataset-faithful Age Demographic Observation Card
    with st.container(border=True):
        st.markdown("**Statistical Summary — Age Group Selection**")
        st.write(get_age_insights(df_age, selected_ages))

st.markdown("---")
st.caption("Source: Revolut debit card transaction data, published by the ONS Real Time Indicators team. Official statistics in development.")
