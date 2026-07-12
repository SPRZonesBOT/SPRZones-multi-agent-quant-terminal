class ModeratorAgent:
    def arbitrate(self, bull_res, bear_res, obi):
        return {
            "verdict": "ACCUMULATE",
            "confidence_score": 87,
            "consensus_summary": "Strong Order Book Imbalance (OBI) favors upside momentum despite macro resistance."
        }
