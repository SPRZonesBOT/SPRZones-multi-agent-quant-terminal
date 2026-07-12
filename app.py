import streamlit as st
import pandas as pd

# Import modular components
from src.data_ingestion.free_feed import FreeDataFeed
from src.agents.bull_agent import BullAgent
from src.agents.bear_agent import BearAgent
from src.agents.moderator_agent import ModeratorAgent
from src.execution.urgency_router import ExecutionRouter
from src.scanners.pead_screener import run_pead_screener
from src.scanners.penny_shock import run_penny_shock_screener

# Page Config
st.set_page_config(page_title="SPRZones Quant Terminal", page_icon="🏛️", layout="wide")

# Initializing Modules
feed = FreeDataFeed()
bull = BullAgent()
bear = BearAgent()
moderator = ModeratorAgent()
router = ExecutionRouter()

# Header
st.title("🏛️ SPRZones Multi-Agent Quant Terminal")
st.caption("Live Global Telemetry & Adaptive Execution Engine")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🤖 Multi-Agent Debate", 
    "⚡ Execution Router (Agent 5)", 
    "🔍 Institutional Scanners", 
    "📈 Macro Telemetry"
])

# TAB 1: Multi-Agent Debate
with tab1:
    st.subheader("Asset Consensus & Agent Debate")
    symbol = st.selectbox("Select Asset:", ["HAL.NS", "SUZLON.NS", "NVDA", "BTC-USD"])
    
    # Mocking live parameters for selection
    obi = 0.82 if symbol == "SUZLON.NS" else 0.35
    bull_res = bull.evaluate([100, 102, 105], obi)
    bear_res = bear.evaluate(0.015, 104.1)
    mod_res = moderator.arbitrate(bull_res, bear_res, obi)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Agent 1 (Bull)", bull_res["signal"], bull_res["momentum"])
    col2.metric("Agent 2 (Bear)", bear_res["signal"], bear_res["risk_level"])
    col3.metric("Agent 3 Verdict", mod_res["verdict"], f"Confidence: {mod_res['confidence_score']}%")
    
    st.info(f"**Moderator Reasoning:** {mod_res['consensus_summary']}")

# TAB 2: Execution Router
with tab2:
    st.subheader("Agent 5: Adaptive Execution Router")
    route_res = router.route_order("SUZLON.NS", alpha=0.045, spread=0.002, vol=0.005)
    
    st.write(f"**Selected Asset:** `{route_res['symbol']}`")
    st.write(f"**Calculated Urgency Index ($U$):** `{route_res['urgency_index']}`")
    st.success(f"**Assigned Execution Regime:** {route_res['regime']}")
    st.write(f"**Execution Action:** {route_res['action']}")

# TAB 3: Scanners
with tab3:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📌 PEAD Screener")
        st.table(run_pead_screener())
    with c2:
        st.subheader("⚡ Penny Shock Screener")
        st.table(run_penny_shock_screener())

# TAB 4: Macro Telemetry
with tab4:
    st.subheader("🌐 Real-time Macro Indicators")
    macro = feed.fetch_macro_telemetry()
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("USD / INR", f"₹{macro.get('USDINR', '83.5')}")
    m2.metric("Crude Oil (WTI)", f"${macro.get('CrudeOil', '82.0')}")
    m3.metric("US Dollar Index (DXY)", f"{macro.get('DXY', '104.1')}")
    m4.metric("Bitcoin (BTC/USD)", f"${macro.get('BTC', '64000')}")
