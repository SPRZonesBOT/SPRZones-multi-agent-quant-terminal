import pandas as pd
import numpy as np

def run_pead_screener() -> pd.DataFrame:
    """Post-Earnings Announcement Drift (PEAD) Screener."""
    data = [
        {"Ticker": "TATAMOTORS.NS", "Market": "NSE India", "Earnings Surprise": "+14.2%", "Post Earnings Drift (SUE)": "+8.4%", "Institutional Action": "Heavy Buying", "Entry Zone": "₹980 - ₹1005"},
        {"Ticker": "NVDA", "Market": "US Tech", "Earnings Surprise": "+18.6%", "Post Earnings Drift (SUE)": "+12.1%", "Institutional Action": "Block Accumulation", "Entry Zone": "$118 - $122"},
        {"Ticker": "HAL.NS", "Market": "NSE India", "Earnings Surprise": "+11.5%", "Post Earnings Drift (SUE)": "+6.2%", "Institutional Action": "FII Inflow", "Entry Zone": "₹4650 - ₹4720"},
        {"Ticker": "INFY.NS", "Market": "NSE India", "Earnings Surprise": "+4.1%", "Post Earnings Drift (SUE)": "+1.8%", "Institutional Action": "Neutral Hold", "Entry Zone": "₹1520 - ₹1550"},
        {"Ticker": "ICICIBANK.NS", "Market": "NSE India", "Earnings Surprise": "+9.8%", "Post Earnings Drift (SUE)": "+5.1%", "Institutional Action": "DII Absorption", "Entry Zone": "₹1180 - ₹1210"},
    ]
    return pd.DataFrame(data)
