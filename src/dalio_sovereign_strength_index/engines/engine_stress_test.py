"""
Sovereign Crisis Simulation Engine.
Enables researchers to inject symmetric fiscal and geopolitical shocks.
"""
import pandas as pd
from dalio_sovereign_strength_index.engines.base_engine import BaseDataEngine

class StressTestEngine(BaseDataEngine):
    def __init__(self, us_debt_shock=0.0, us_military_shock=0.0, cn_debt_shock=0.0, cn_military_shock=0.0):
        self.us_debt_shock = us_debt_shock
        self.us_military_shock = us_military_shock
        self.cn_debt_shock = cn_debt_shock
        self.cn_military_shock = cn_military_shock

    def fetch_data(self, start_yr: int, end_yr: int) -> pd.DataFrame:
        """Generates standard baseline tracking data mixed with custom shock parameters."""
        records = []
        for yr in range(int(start_yr), int(end_yr) + 1):
            us_debt = 121.5 + (yr - start_yr) * 1.4
            us_mil = 3.4
            cn_debt = 76.8 + (yr - start_yr) * 2.3
            cn_mil = 1.7
            
            # Apply symmetric slider deltas to the target forecast frontier row
            if yr == int(end_yr):
                us_debt += self.us_debt_shock
                us_mil += self.us_military_shock
                cn_debt += self.cn_debt_shock
                cn_mil += self.cn_military_shock

            records.append({
                'year': int(yr),
                'Country': 'US',
                'Debt_To_GDP': us_debt,
                'Military_Exp': us_mil
            })
            records.append({
                'year': int(yr),
                'Country': 'CN',
                'Debt_To_GDP': cn_debt,
                'Military_Exp': cn_mil
            })
        return pd.DataFrame(records)
