import pandas as pd

def run_pead_screener():
    return pd.DataFrame({
        "Ticker": ["TATAMOTORS.NS", "RELIANCE.NS", "INFY.NS"],
        "Earnings Surprise": ["+12.4%", "+5.1%", "+8.3%"],
        "Drift Volatility": ["High", "Medium", "Low"]
    })
