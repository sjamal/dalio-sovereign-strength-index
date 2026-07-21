"""
Streamlit Web Analytics Presentation Interface.
Generates charts for comparative nation tracking.
"""
import streamlit as st
import pandas as pd
from dalio_sovereign_strength_index.pipeline import MacroDataPipeline
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

st.set_page_config(page_title="Sovereign Strength Index Gauge", layout="wide", page_icon="📈")

st.title("🧠 Sovereign Strength Index Dashboard")
st.markdown("Automated quantitative tracking for the United States and China based on multi-determinant macro indices.")

# Sidebar Configurations
st.sidebar.header("Pipeline Controls")
start_yr = st.sidebar.slider("Start Horizon Year", 2010, 2024, 2018)
end_yr = st.sidebar.slider("End Horizon Year", 2025, 2026, 2025)

@st.cache_data
def run_cached_pipeline(s, e):
    pipeline = MacroDataPipeline()
    engine = DalioAnalysisEngine()
    
    raw = pipeline.execute_pipeline(s, e)
    scored = engine.calculate_power_index(raw)
    scored['Stage'] = scored.apply(engine.classify_lifecycle_stage, axis=1)
    return scored

try:
    with st.spinner("Processing remote pipelines..."):
        data = run_cached_pipeline(start_yr, end_yr)
        
    # Isolate records for side-by-side comparison
    us_data = data[data['Country'] == 'US'].sort_values('year')
    cn_data = data[data['Country'] == 'CN'].sort_values('year')
    
    # Dashboard Grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🇺🇸 United States State Matrix")
        latest_us = us_data.iloc[-1]
        st.metric(label="Total Strength Index Score", value=f"{latest_us['Dalio_Power_Index']:.3f}")
        st.info(f"**Calculated Lifecycle State**: {latest_us['Stage']}")
        
    with col2:
        st.subheader("🇨🇳 China State Matrix")
        latest_cn = cn_data.iloc[-1]
        st.metric(label="Total Strength Index Score", value=f"{latest_cn['Dalio_Power_Index']:.3f}")
        st.warning(f"**Calculated Lifecycle State**: {latest_cn['Stage']}")
        
    st.subheader("Relative System Trajectory Over Time")
    # Clean pivoting for time-series charts
    chart_data = data.pivot(index='year', columns='Country', values='Dalio_Power_Index')
    st.line_chart(chart_data)
    
    st.subheader("📊 Underlying Analytical Indicators Matrix")
    st.dataframe(data[['year', 'Country', 'Dalio_Power_Index', 'Debt_To_GDP', 'Military_Exp', 'Stage']], use_container_width=True)

except Exception as e:
    st.error(f"Failed to execute visualization layer pipeline: {e}")
