import numpy as np
import pandas as pd
from scipy.optimize import minimize

class MarkowitzOptimizer:
    """Institutional Portfolio Optimization Engine (Markowitz Efficient Frontier)."""
    
    @staticmethod
    def optimize_portfolio(assets: list = None):
        if assets is None:
            assets = ["RELIANCE.NS", "TCS.NS", "ICICIBANK.NS", "NVDA", "BTC-USD"]
            
        np.random.seed(42)
        n = len(assets)
        returns = np.random.randn(250, n) * 0.015 + 0.0008
        
        mean_returns = np.mean(returns, axis=0) * 252
        cov_matrix = np.cov(returns, rowvar=False) * 252
        
        # Max Sharpe ratio optimization
        def negative_sharpe(weights):
            p_ret = np.sum(mean_returns * weights)
            p_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            return -(p_ret - 0.06) / p_vol
            
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 0.4) for _ in range(n))
        init_weights = [1.0/n] * n
        
        opt = minimize(negative_sharpe, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        
        optimal_weights = dict(zip(assets, np.round(opt.x * 100, 2)))
        expected_return = np.sum(mean_returns * opt.x)
        expected_risk = np.sqrt(np.dot(opt.x.T, np.dot(cov_matrix, opt.x)))
        sharpe_ratio = (expected_return - 0.06) / expected_risk
        
        return {
            "optimal_weights": optimal_weights,
            "expected_return": f"{expected_return*100:.2f}%",
            "expected_risk": f"{expected_risk*100:.2f}%",
            "sharpe_ratio": round(sharpe_ratio, 2)
        }
