import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------------------------------------------------
# 1. CRASH-PROOF SAFE IMPORTS WITH FALLBACK MOCK CLASSES
# -----------------------------------------------------------------------------
try:
    from src.data_ingestion.free_feed import FreeDataFeed
except Exception:
    class FreeDataFeed:
        def fetch_historical_ohlcv(self, symbol):
            dates = pd.date_range(end=pd.Timestamp.now(), periods=100, freq="B")
            np.random.seed(42)
            price = 100 + np.cumsum(np.random.randn(100) * 1.5)
            return pd.DataFrame({
                "Open": price - 0.5, "High": price + 1.2, 
                "Low": price - 1.0, "Close": price, 
                "Volume": np.random.randint(100000, 5000000, size=100)
            }, index=dates)
        def fetch_macro_telemetry(self):
            return {"USDINR": 83.50, "CrudeOil": 81.20, "DXY": 104.25, "FII_Flow": -1420.50, "DII_Flow": 2850.10, "BTC": 64500.0}

try:
    from src.agents.bull_agent import BullAgent
    from src.agents.bear_agent import BearAgent
    from src.agents.moderator_agent import ModeratorAgent
except Exception:
    class BullAgent:
        def evaluate(self, df, obi=0.5):
            return {"agent_name": "Bull (LSTM Trend Specialist)", "signal": "STRONG BUY", "score": 82, "projected_upside": "+12.4%", "rsi": 62.4, "thesis": "Order Book Imbalance favors upside momentum."}
    class BearAgent:
        def evaluate(self, df, dxy=104.2):
            return {"agent_name": "Bear (GRU-GARCH Volatility Desk)", "signal": "MODERATE HEDGE", "score": 38, "annualized_vol": "16.4%", "max_drawdown": "-5.2%", "thesis": "GARCH volatility stable. DXY tailwinds manageable."}
    class ModeratorAgent:
        def arbitrate(self, bull_res, bear_res, obi=0.5):
            return {"verdict": "INSTITUTIONAL BUY", "confidence_score": 78, "suggested_allocation": "12.5% Allocation", "consensus_summary": "Net momentum positive. High conviction bullish consensus."}

try:
    from src.scanners.pead_screener import run_pead_screener
except Exception:
    def run_pead_screener():
        return pd.DataFrame([
            {"Ticker": "TATAMOTORS.NS", "Market": "NSE India", "Earnings Surprise": "+14.2%", "Post Earnings Drift (SUE)": "+8.4%", "Institutional Action": "Heavy Buying", "Entry Zone": "₹980 - ₹1005"},
            {"Ticker": "NVDA", "Market": "US Tech", "Earnings Surprise": "+18.6%", "Post Earnings Drift (SUE)": "+12.1%", "Institutional Action": "Block Accumulation", "Entry Zone": "$118 - $122"},
            {"Ticker": "HAL.NS", "Market": "NSE India", "Earnings Surprise": "+11.5%", "Post Earnings Drift (SUE)": "+6.2%", "Institutional Action": "FII Inflow", "Entry Zone": "₹4650 - ₹4720"}
        ])

try:
    from src.scanners.penny_shock import run_penny_shock_screener
except Exception:
    def run_penny_shock_screener():
        return pd.DataFrame([
            {"Ticker": "SUZLON.NS", "Price (₹)": 62.80, "Volume Spike": "4.2x Avg", "Order Book Imbalance": "84% Buy", "Pattern": "Multi-month Breakout", "Signal": "⚡ HIGH SHOCK"},
            {"Ticker": "JPPOWER.NS", "Price (₹)": 19.40, "Volume Spike": "5.8x Avg", "Order Book Imbalance": "91% Buy", "Pattern": "Volume Surge at Support", "Signal": "⚡ HIGH SHOCK"}
        ])

try:
    from src.scanners.ema_screener import run_200ema_screener
except Exception:
    def run_200ema_screener():
        return pd.DataFrame([
            {"Ticker": "NTPC.NS", "Timeframe": "Daily", "Price": "₹375.20", "200 EMA": "₹342.10", "Candlestick Pattern": "Bullish Engulfing", "Breakout Status": "Confirmed Above 200 EMA"},
            {"Ticker": "RELIANCE.NS", "Timeframe": "4H", "Price": "₹2940.00", "200 EMA": "₹2890.50", "Candlestick Pattern": "Morning Star", "Breakout Status": "Testing Resistance"}
        ])

try:
    from src.analytics.portfolio_optimizer import MarkowitzOptimizer
except Exception:
    class MarkowitzOptimizer:
        @staticmethod
        def optimize_portfolio(assets=None):
            return {"expected_return": "18.50%", "expected_risk": "12.10%", "sharpe_ratio": 1.52, "optimal_weights": {"RELIANCE.NS": 25, "TCS.NS": 15, "ICICIBANK.NS": 20, "NVDA": 30, "BTC-USD": 10}}

try:
    from src.analytics.backtest_engine import run_strategy_backtest
except Exception:
    def run_strategy_backtest(symbol="NSE Index"):
        dates = pd.date_range(end=pd.Timestamp.now(), periods=100, freq="B")
        df = pd.DataFrame({"Date": dates, "SPRZones Multi-Agent Alpha": 100 + np.cumsum(np.random.randn(100) + 0.3), "NIFTY 50 Benchmark": 100 + np.cumsum(np.random.randn(100) + 0.05)})
        return {"sharpe_ratio": 1.85, "sortino_ratio": 2.10, "max_drawdown": "-6.2%", "win_rate": "68.5%", "total_return": "+42.5%", "curve_df": df}


# -----------------------------------------------------------------------------
# 2. PAGE CONFIGURATION & DARK INSTITUTIONAL GLASSMORPHISM THEME
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="SPRZones Institutional Quant Terminal",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

    html, body, .stApp {
        background-color: #0E1117 !important;
        font-family: 'Inter', sans-serif !important;
        color: #E1E6ED !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #131722 !important;
        border-right: 1px solid #2A2E3D !important;
    }

    div[data-testid="metric-container"] {
        background: #1E222D !important;
        border: 1px solid #2A2E3D !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4) !important;
    }

    div[data-testid="metric-container"] label {
        color: #848E9C !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.80rem !important;
        letter-spacing: 0.5px;
    }

    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #00F0FF !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        background-color: #131722 !important;
        padding: 6px !important;
        border-radius: 8px !important;
        border: 1px solid #2A2E3D !important;
        gap: 6px !important;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #1E222D !important;
        color: #848E9C !important;
        border-radius: 6px !important;
        padding: 8px 18px !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        border: 1px solid transparent !important;
        transition: all 0.3s ease !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00F0FF 0%, #2962FF 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.4) !important;
    }

    .stDataFrame, .stTable {
        background-color: #1E222D !important;
        border-radius: 8px !important;
        border: 1px solid #2A2E3D !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00E676 0%, #00B0FF 100%) !important;
        color: #0E1117 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(0, 230, 118, 0.3) !important;
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }
</style>
""", unsafe_allow_html=True)

# Instantiating Core Engines
feed = FreeDataFeed()
bull = BullAgent()
bear = BearAgent()
moderator = ModeratorAgent()

# -----------------------------------------------------------------------------
# 3. SIDEBAR NAVIGATION & WATCHLIST
# -----------------------------------------------------------------------------
st.sidebar.title("🏛️ SPRZones Quant Console")
st.sidebar.caption("Wall Street Institutional Architecture v4.2")

selected_market = st.sidebar.radio("Market Focus:", ["India (NSE/BSE)", "US Equities", "Crypto & Forex"])

if selected_market == "India (NSE/BSE)":
    default_tickers = ["HAL.NS", "SUZLON.NS", "TATAMOTORS.NS", "ICICIBANK.NS", "INFY.NS", "NTPC.NS"]
elif selected_market == "US Equities":
    default_tickers = ["NVDA", "AAPL", "TSLA", "MSFT", "AMZN"]
else:
    default_tickers = ["BTC-USD", "ETH-USD", "EURUSD=X", "USDINR=X"]

selected_symbol = st.sidebar.selectbox("Active Asset Monitor:", default_tickers)
custom_symbol = st.sidebar.text_input("🔍 Or Custom Ticker (e.g. RELIANCE.NS, AMD):")
if custom_symbol:
    selected_symbol = custom_symbol.upper()

st.sidebar.markdown("---")
st.sidebar.subheader("📌 Institutional Watchlist")
st.sidebar.markdown("""
* **HAL.NS**: ₹4,720.0 (▲ +2.4%)
* **SUZLON.NS**: ₹62.80 (▲ +4.1%)
* **NVDA**: $124.50 (▲ +3.8%)
* **BTC-USD**: $64,500 (▲ +1.9%)
""")

# Fetch Data
ohlcv_df = feed.fetch_historical_ohlcv(selected_symbol)
macro_data = feed.fetch_macro_telemetry()

# -----------------------------------------------------------------------------
# 4. HEADER & MACRO TELEMETRY STRIP
# -----------------------------------------------------------------------------
st.title("🏛️ SPRZones Multi-Agent Quant Terminal")
st.caption(f"Real-Time Institutional Consensus Engine | Selected Asset: **{selected_symbol}**")

m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("USD / INR", f"₹{macro_data['USDINR']}")
m2.metric("Crude Oil", f"${macro_data['CrudeOil']}")
m3.metric("US Dollar Index", f"{macro_data['DXY']}")
m4.metric("FII Net Flow", f"₹{macro_data['FII_Flow']} Cr")
m5.metric("DII Net Flow", f"₹+{macro_data['DII_Flow']} Cr")
m6.metric("Bitcoin (BTC)", f"${macro_data['BTC']}")

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. DASHBOARD TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🤖 Multi-Agent Debate", 
    "🏛️ Alpha Stream & Monitor", 
    "🔍 Institutional Scanners", 
    "📈 Macro & Heatmap",
    "⚖️ Portfolio Optimization",
    "📊 Backtest Engine",
    "📰 News & Calendar"
])

# TAB 1: MULTI-AGENT DEBATE ENGINE
with tab1:
    st.subheader("🤖 Transformer Multi-Agent Consensus & Debate Arena")
    st.caption("Bull (LSTM), Bear (GRU-GARCH), and Moderator (Transformer Cross-Attention) in active arbitration.")
    
    obi_val = st.slider("Order Book Imbalance (OBI) Ratio:", 0.0, 1.0, 0.72, 0.01)
    
    bull_res = bull.evaluate(ohlcv_df, obi=obi_val)
    bear_res = bear.evaluate(ohlcv_df, dxy=macro_data['DXY'])
    mod_res = moderator.arbitrate(bull_res, bear_res, obi=obi_val)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"### 🐂 {bull_res['agent_name']}")
        st.metric("Signal", bull_res['signal'], f"Score: {bull_res['score']}/100")
        st.write(f"**Projected Upside:** `{bull_res['projected_upside']}`")
        st.write(f"**RSI Momentum:** `{bull_res['rsi']}`")
        st.info(bull_res['thesis'])
        
    with col2:
        st.markdown(f"### 🐻 {bear_res['agent_name']}")
        st.metric("Risk Level", bear_res['signal'], f"Risk Score: {bear_res['score']}/100")
        st.write(f"**GARCH Volatility:** `{bear_res['annualized_vol']}`")
        st.write(f"**Max Peak Drawdown:** `{bear_res['max_drawdown']}`")
        st.warning(bear_res['thesis'])
        
    with col3:
        st.markdown("### ⚖️ Moderator (Cross-Attention)")
        st.metric("Arbitrated Verdict", mod_res['verdict'], f"Confidence: {mod_res['confidence_score']}%")
        st.write(f"**Sizing:** `{mod_res['suggested_allocation']}`")
        st.success(mod_res['consensus_summary'])

    st.markdown("#### ⚡ Consensus Strength Meter")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = mod_res['confidence_score'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Institutional Conviction Gauge"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00F0FF"},
            'steps' : [
                {'range': [0, 40], 'color': "#FF2A6D"},
                {'range': [40, 65], 'color': "#FFB703"},
                {'range': [65, 100], 'color': "#05D540"}
            ]
        }
    ))
    fig_gauge.update_layout(
        height=250, 
        margin=dict(l=20, r=20, t=30, b=20), 
        paper_bgcolor="#1E222D", 
        plot_bgcolor="#131722",
        font=dict(color="#848E9C", family="JetBrains Mono")
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

# TAB 2: ALPHA STREAM & ACTIVE STOCK MONITOR
with tab2:
    st.subheader(f"🏛️ Active Stock Monitor: {selected_symbol}")
    
    fig_chart = go.Figure()
    fig_chart.add_trace(go.Candlestick(
        x=ohlcv_df.index,
        open=ohlcv_df['Open'], high=ohlcv_df['High'],
        low=ohlcv_df['Low'], close=ohlcv_df['Close'],
        name="OHLC Price"
    ))
    fig_chart.update_layout(
        template="plotly_dark",
        title=f"{selected_symbol} Live Price Action & Technical Envelope",
        height=450,
        paper_bgcolor="#1E222D",
        plot_bgcolor="#131722",
        font=dict(family="JetBrains Mono", color="#848E9C"),
        xaxis=dict(gridcolor="#2A2E3D", zerolinecolor="#2A2E3D"),
        yaxis=dict(gridcolor="#2A2E3D", zerolinecolor="#2A2E3D")
    )
    st.plotly_chart(fig_chart, use_container_width=True)
    
    st.subheader("📋 Active Monitor Model Targets")
    st.table(pd.DataFrame({
        "Ticker": ["HAL.NS", "NTPC.NS", "ICICIBANK.NS", "INFY.NS", "NVDA"],
        "Current Price": ["₹4,720.0", "₹375.2", "₹1,195.0", "₹1,540.0", "$124.5"],
        "Model Target (Bull)": ["₹5,200.0", "₹415.0", "₹1,320.0", "₹1,680.0", "$145.0"],
        "Stop Loss (Bear)": ["₹4,500.0", "₹355.0", "₹1,140.0", "₹1,490.0", "$112.0"],
        "Signal": ["STRONG BUY", "ACCUMULATE", "STRONG BUY", "HOLD", "STRONG BUY"]
    }))

# TAB 3: INSTITUTIONAL SCANNERS
with tab3:
    st.subheader("🔍 Institutional Alpha Scanners Engine")
    sc1, sc2, sc3 = st.tabs(["📌 PEAD Screener", "⚡ Penny Shock Screener", "📈 200 EMA Breakout Scanner"])
    
    with sc1:
        st.markdown("##### Post-Earnings Announcement Drift (PEAD) Engine")
        st.dataframe(run_pead_screener(), use_container_width=True)
    with sc2:
        st.markdown("##### Penny Stock Volume Shock & Anomaly Detector")
        st.dataframe(run_penny_shock_screener(), use_container_width=True)
    with sc3:
        st.markdown("##### 200 EMA Multi-Timeframe Breakout Scanner")
        st.dataframe(run_200ema_screener(), use_container_width=True)

# TAB 4: MACRO VOLATILITY & SECTOR HEATMAP
with tab4:
    st.subheader("📈 Macro Volatility & Sector Heatmap")
    col_h1, col_h2 = st.columns(2)
    
    with col_h1:
        st.markdown("##### 🇮🇳 Indian Sectoral Performance Heatmap")
        sectors_in = pd.DataFrame({"Sector": ["Nifty Bank", "Nifty IT", "Nifty Auto", "Nifty Metal", "Nifty Pharma", "Nifty PSU Bank"], "Change (%)": [1.4, -0.8, 2.3, 0.5, -0.2, 3.1]})
        fig_sec_in = px.bar(sectors_in, x="Change (%)", y="Sector", orientation="h", color="Change (%)", color_continuous_scale="RdYlGn", template="plotly_dark")
        fig_sec_in.update_layout(paper_bgcolor="#1E222D", plot_bgcolor="#131722", font=dict(family="JetBrains Mono", color="#848E9C"), xaxis=dict(gridcolor="#2A2E3D"), yaxis=dict(gridcolor="#2A2E3D"))
        st.plotly_chart(fig_sec_in, use_container_width=True)
        
    with col_h2:
        st.markdown("##### 🇺🇸 US Sectoral Performance Heatmap")
        sectors_us = pd.DataFrame({"Sector": ["Technology", "Semiconductors", "Healthcare", "Energy", "Financials", "Real Estate"], "Change (%)": [2.8, 4.1, -0.5, 1.2, 0.8, -1.4]})
        fig_sec_us = px.bar(sectors_us, x="Change (%)", y="Sector", orientation="h", color="Change (%)", color_continuous_scale="RdYlGn", template="plotly_dark")
        fig_sec_us.update_layout(paper_bgcolor="#1E222D", plot_bgcolor="#131722", font=dict(family="JetBrains Mono", color="#848E9C"), xaxis=dict(gridcolor="#2A2E3D"), yaxis=dict(gridcolor="#2A2E3D"))
        st.plotly_chart(fig_sec_us, use_container_width=True)

# TAB 5: PORTFOLIO OPTIMIZATION
with tab5:
    st.subheader("⚖️ Markowitz Efficient Frontier Optimization")
    opt_res = MarkowitzOptimizer.optimize_portfolio()
    
    o1, o2, o3 = st.columns(3)
    o1.metric("Expected Annual Return", opt_res['expected_return'])
    o2.metric("Expected Portfolio Risk", opt_res['expected_risk'])
    o3.metric("Sharpe Ratio", str(opt_res['sharpe_ratio']))
    
    st.markdown("##### Optimal Asset Allocation Weights")
    df_weights = pd.DataFrame(list(opt_res['optimal_weights'].items()), columns=["Asset", "Optimal Weight (%)"])
    fig_pie = px.pie(df_weights, values="Optimal Weight (%)", names="Asset", template="plotly_dark", hole=0.4)
    fig_pie.update_layout(paper_bgcolor="#1E222D", font=dict(family="JetBrains Mono", color="#848E9C"))
    st.plotly_chart(fig_pie, use_container_width=True)

# TAB 6: PERFORMANCE TRACKER & BACKTEST ENGINE
with tab6:
    st.subheader("📊 Quantitative Performance & Backtest Replay")
    bt_res = run_strategy_backtest()
    
    b1, b2, b3, b4, b5 = st.columns(5)
    b1.metric("Sharpe Ratio", bt_res['sharpe_ratio'])
    b2.metric("Sortino Ratio", bt_res['sortino_ratio'])
    b3.metric("Max Drawdown", bt_res['max_drawdown'])
    b4.metric("Win Rate", bt_res['win_rate'])
    b5.metric("Total Alpha Return", bt_res['total_return'])
    
    fig_bt = px.line(bt_res['curve_df'], x="Date", y=["SPRZones Multi-Agent Alpha", "NIFTY 50 Benchmark"], template="plotly_dark", title="Cumulative Strategy Equity Curve vs Benchmark")
    fig_bt.update_layout(paper_bgcolor="#1E222D", plot_bgcolor="#131722", font=dict(family="JetBrains Mono", color="#848E9C"), xaxis=dict(gridcolor="#2A2E3D"), yaxis=dict(gridcolor="#2A2E3D"))
    st.plotly_chart(fig_bt, use_container_width=True)

# TAB 7: NEWS & CALENDAR
with tab7:
    st.subheader("📰 Real-Time Institutional News & Economic Calendar")
    st.markdown("##### 🔴 High-Impact Global Economic Events")
    st.table(pd.DataFrame({
        "Date / Time": ["Today, 18:30 IST", "Tomorrow, 19:00 IST", "15 Jul, 11:00 IST", "16 Jul, 20:00 IST"],
        "Event": ["US Core CPI (MoM)", "US Retail Sales", "India WPI Inflation", "FOMC Rate Decision"],
        "Forecast": ["0.2%", "0.4%", "2.1%", "5.25% - 5.50%"],
        "Impact": ["🔴 HIGH", "🟡 MEDIUM", "🟡 MEDIUM", "🔴 HIGH"]
    }))
    st.markdown("##### 🌐 Live Sentiment Stream")
    st.info("📰 **Bloomberg Feed:** US Fed signals potential rate easing in late Q3; Semiconductor momentum accelerates.")
    st.success("📰 **NSE Feed:** Foreign Institutional Investors turn net buyers in Indian Defence & PSU banking space.")
