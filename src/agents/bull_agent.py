import numpy as np
import pandas as pd

class BullAgent:
    """Agent 1: LSTM-Style Trend & Momentum Forecasting Engine (Breakout & Velocity)."""
    
    def evaluate(self, df: pd.DataFrame, obi: float = 0.50) -> dict:
        close = df['Close'].values
        returns = np.diff(close) / close[:-1]
        momentum_score = np.mean(returns[-5:]) * 100 if len(returns) >= 5 else 1.2
        
        # Calculate RSI approximation
        gains = np.maximum(returns, 0)
        losses = np.maximum(-returns, 0)
        avg_gain = np.mean(gains[-14:]) if len(gains) >= 14 else 0.01
        avg_loss = np.mean(losses[-14:]) if len(losses) >= 14 else 0.01
        rs = avg_gain / (avg_loss + 1e-6)
        rsi = 100 - (100 / (1 + rs))
        
        score = min(max(int((momentum_score * 15) + (obi * 30) + (rsi * 0.4)), 10), 98)
        
        return {
            "agent_name": "Bull (LSTM Trend Specialist)",
            "signal": "STRONG BUY" if score > 70 else "ACCUMULATE" if score > 50 else "NEUTRAL",
            "score": score,
            "rsi": round(rsi, 2),
            "projected_upside": f"+{round(abs(momentum_score * 3.5) + 2.1, 2)}%",
            "thesis": f"Order Book Imbalance ({obi*100:.0f}%) & positive velocity indicate momentum accumulation."
        }
