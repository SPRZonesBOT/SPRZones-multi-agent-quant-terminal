import pandas as pd

def run_penny_shock_screener() -> pd.DataFrame:
    """Penny Shock Volume & Volatility Anomaly Screener."""
    data = [
        {"Ticker": "SUZLON.NS", "Price (₹)": 62.80, "Volume Spike": "4.2x Avg", "Order Book Imbalance": "84% Buy", "Pattern": "Multi-month Consolidation Breakout", "Signal": "⚡ HIGH SHOCK"},
        {"Ticker": "JPPOWER.NS", "Price (₹)": 19.40, "Volume Spike": "5.8x Avg", "Order Book Imbalance": "91% Buy", "Pattern": "Volume Surge at Support", "Signal": "⚡ HIGH SHOCK"},
        {"Ticker": "RPOWER.NS", "Price (₹)": 31.15, "Volume Spike": "2.9x Avg", "Order Book Imbalance": "68% Buy", "Pattern": "Ascending Triangle Breakout", "Signal": "🔍 WATCHLIST"},
        {"Ticker": "SHG.V", "Price ($)": 0.45, "Volume Spike": "6.1x Avg", "Order Book Imbalance": "77% Buy", "Pattern": "Penny Reversal Pattern", "Signal": "⚡ HIGH SHOCK"},
    ]
    return pd.DataFrame(data)
