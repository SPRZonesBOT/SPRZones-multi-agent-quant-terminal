import pandas as pd

def run_penny_shock_screener():
    return pd.DataFrame({
        "Ticker": ["SUZLON.NS", "JPPOWER.NS", "RPOWER.NS"],
        "Volume Shock": ["3.4x", "5.1x", "2.8x"],
        "Breakout Signal": ["Confirmed", "Watchlist", "Confirmed"]
    })
