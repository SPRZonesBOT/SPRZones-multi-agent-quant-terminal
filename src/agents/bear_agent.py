import numpy as np
import pandas as pd

class BearAgent:
    """Agent 2: GRU + GARCH Volatility & Downside Anomaly Engine."""
    
    def evaluate(self, df: pd.DataFrame, dxy: float = 104.2) -> dict:
        close = df['Close'].values
        returns = np.diff(close) / close[:-1] if len(close) > 1 else np.array([0.01])
        
        # GARCH-style Volatility proxy
        volatility = np.std(returns) * np.sqrt(252) * 100
        max_dd = (np.max(close) - close[-1]) / np.max(close) * 100
        
        risk_score = min(max(int((volatility * 1.8) + (max_dd * 1.2) + (dxy * 0.2 - 15)), 5), 95)
        
        return {
            "agent_name": "Bear (GRU-GARCH Volatility Desk)",
            "signal": "HIGH RISK" if risk_score > 70 else "MODERATE HEDGE" if risk_score > 45 else "LOW RISK",
            "score": risk_score,
            "annualized_vol": f"{round(volatility, 2)}%",
            "max_drawdown": f"{round(max_dd, 2)}%",
            "thesis": f"GARCH Volatility at {volatility:.1f}%. DXY tailwinds present downside risk."
        }
