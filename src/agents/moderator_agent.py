class ModeratorAgent:
    """Agent 3: Transformer Cross-Attention Arbitration & Portfolio Sizing."""
    
    def arbitrate(self, bull_res: dict, bear_res: dict, obi: float, news_sentiment: float = 0.65) -> dict:
        # Cross-attention weighting simulation
        w_bull = 0.45
        w_bear = 0.35
        w_sentiment = 0.20
        
        bull_val = bull_res["score"]
        bear_val = 100 - bear_res["score"]  # Inverse risk score
        sent_val = news_sentiment * 100
        
        consensus_score = int((bull_val * w_bull) + (bear_val * w_bear) + (sent_val * w_sentiment))
        
        if consensus_score >= 70:
            verdict = "INSTITUTIONAL BUY"
            alloc = "12.5% Portfolio Allocation (Aggressive)"
        elif consensus_score >= 50:
            verdict = "TACTICAL ACCUMULATE"
            alloc = "6.0% Portfolio Allocation (Moderate)"
        elif consensus_score >= 35:
            verdict = "HOLD / COVER SHORTS"
            alloc = "2.0% Defensive Position"
        else:
            verdict = "LIQUIDATE / SHORT"
            alloc = "0.0% (Capital Preservation)"
            
        return {
            "verdict": verdict,
            "confidence_score": consensus_score,
            "bull_strength": bull_val,
            "bear_strength": bear_res["score"],
            "suggested_allocation": alloc,
            "consensus_summary": f"Cross-attention weights favor {verdict}. Bull momentum score ({bull_val}) neutralized against Bear risk ({bear_res['score']})."
        }
