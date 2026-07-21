"""
Streamlit Web Analytics Presentation Interface.
Symmetric coloring and advanced tabbed performance layouts.
"""
import streamlit as st
import pandas as pd
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

# Set up browser window parameters
st.set_page_config(page_title="Sovereign Strength Index Gauge", layout="wide", page_icon="📈")

st.title("🧠 Sovereign Strength Index Dashboard")
st.markdown("Automated quantitative tracking for the United States and China based on multi-determinant macro indices.")

# ----------------------------------------------------------------------
# SIDEBAR CONTROLS (SYMMETRIC SHOCKS)
# ----------------------------------------------------------------------
st.sidebar.header("Timeline Focus")
start_yr = st.sidebar.slider("Start Horizon Year", 2010, 2024, 2018)
end_yr = st.sidebar.slider("End Horizon Year", 2025, 2026, 2025)

st.sidebar.header("🇺🇸 US Crisis Shocks")
us_debt_shock = st.sidebar.slider("US Debt Shock Addition (%)", 0, 100, 0, key="us_debt")
us_mil_shock = st.sidebar.slider("US Military Budget Alteration (% GDP)", -2.0, 5.0, 0.0, key="us_mil")

st.sidebar.header("🇨🇳 China Crisis Shocks")
cn_debt_shock = st.sidebar.slider("China Debt Shock Addition (%)", 0, 100, 0, key="cn_debt")
cn_mil_shock = st.sidebar.slider("China Military Budget Alteration (% GDP)", -2.0, 5.0, 0.0, key="cn_mil")

# ----------------------------------------------------------------------
# PIPELINE COMPUTATION LAYER
# ----------------------------------------------------------------------
@st.cache_data
def run_stress_pipeline(s, e, us_ds, us_ms, cn_ds, cn_ms):
    """Executes the modular data engine and assigns lifecycle stages."""
    from dalio_sovereign_strength_index.engines.engine_stress_test import StressTestEngine
    engine = DalioAnalysisEngine()
    
    stress_pipeline = StressTestEngine(
        us_debt_shock=us_ds, us_military_shock=us_ms, 
        cn_debt_shock=cn_ds, cn_military_shock=cn_ms
    )
    raw = stress_pipeline.fetch_data(s, e)
    scored = engine.calculate_power_index(raw)
    scored['Stage'] = scored.apply(engine.classify_lifecycle_stage, axis=1)
    return scored

# ----------------------------------------------------------------------
# DASHBOARD PRESENTATION LAYER
# ----------------------------------------------------------------------
try:
    with st.spinner("Processing scenario models..."):
        data = run_stress_pipeline(start_yr, end_yr, us_debt_shock, us_mil_shock, cn_debt_shock, cn_mil_shock)
        
    us_data = data[data['Country'] == 'US'].sort_values('year')
    cn_data = data[data['Country'] == 'CN'].sort_values('year')
    
    # Build core presentation grid columns
    col1, col2 = st.columns(2)
    
    # --- UNITED STATES STATUS PANEL ---
    with col1:
        st.subheader("🇺🇸 United States State Matrix")
        latest_us = us_data.iloc[-1]
        st.metric(label="Total Strength Index Score", value=f"{latest_us['Dalio_Power_Index']:.3f}")
        
        # Unified Blue status banner rendering layout via standard HTML blocks
        st.markdown(
            f'<div style="background-color:#1f77b4; color:white; padding:12px; border-radius:6px; margin-bottom:15px;">'
            f'<strong>Calculated Lifecycle State</strong>: {latest_us["Stage"]}</div>', 
            unsafe_allow_html=True
        )
        
        sub_us1, sub_us2 = st.columns(2)
        sub_us1.metric(label="Debt to GDP Ratio", value=f"{latest_us['Debt_To_GDP']:.1f}%")
        sub_us2.metric(label="Military Budget (% GDP)", value=f"{latest_us['Military_Exp']:.2f}%")
        
    # --- CHINA STATUS PANEL ---
    with col2:
        st.subheader("🇨🇳 China State Matrix")
        latest_cn = cn_data.iloc[-1]
        st.metric(label="Total Strength Index Score", value=f"{latest_cn['Dalio_Power_Index']:.3f}")
        
        # Unified Red status banner rendering layout via standard HTML blocks
        st.markdown(
            f'<div style="background-color:#d62728; color:white; padding:12px; border-radius:6px; margin-bottom:15px;">'
            f'<strong>Calculated Lifecycle State</strong>: {latest_cn["Stage"]}</div>', 
            unsafe_allow_html=True
        )
        
        sub_cn1, sub_cn2 = st.columns(2)
        sub_cn1.metric(label="Debt to GDP Ratio", value=f"{latest_cn['Debt_To_GDP']:.1f}%")
        sub_cn2.metric(label="Military Budget (% GDP)", value=f"{latest_cn['Military_Exp']:.2f}%")
        
    # --- TIME-SERIES VISUAL CHART ---
    st.subheader("Relative System Trajectory Over Time")
    chart_data = data.pivot(index='year', columns='Country', values='Dalio_Power_Index')
    
    # Enforce explicit symmetric color hex keys (Blue for US, Red for China)
    st.line_chart(chart_data, color=["#d62728", "#1f77b4"])
    
    # ----------------------------------------------------------------------
    # DIAGNOSTIC OPERATION TABS SECTION
    # ----------------------------------------------------------------------
    st.markdown("---")
    st.subheader("⚙️ System Performance and Diagnostic Operations")
    
    tab1, tab2 = st.tabs(["Superpower Macro Trends", "MCP Server Automation Performance"])
    
    with tab1:
        st.markdown("### 📊 Active Superpower System Data Summary")
        st.markdown(
            "Review the comprehensive data matrix below tracking multi-determinant vectors. "
            "Use the side sliders to simulate crisis shocks and observe how they alter the trajectory trends "
            "and lifecycle stages on the tracking chart layout above."
        )
        st.dataframe(data[['year', 'Country', 'Dalio_Power_Index', 'Debt_To_GDP', 'Military_Exp', 'Stage']], width='stretch')
        
    with tab2:
        st.markdown("### Model Context Protocol (MCP) Stream Velocity Trends")
        try:
            bench_data = pd.read_csv("docs/mcp_performance_trends.csv")
            bench_data = bench_data.set_index('Iteration')
            st.line_chart(bench_data)
            st.caption("Tracks engine response velocities in milliseconds across consecutive automated JSON-RPC loops.")
        except FileNotFoundError:
            st.info("💡 Run `python scripts/mcp_bench_reporter.py` to generate the performance trends plot data.")

except Exception as e:
    st.error(f"Failed to execute visualization layer pipeline: {e}")
