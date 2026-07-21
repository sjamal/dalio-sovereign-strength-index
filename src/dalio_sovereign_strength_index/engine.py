"""
Quantitative Mathematical Engine.
Processes macro variables, yields power index arrays, and gauges lifecycle stages.
"""
import numpy as np
import pandas as pd

class DalioAnalysisEngine:
    @staticmethod
    def calculate_power_index(df: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms raw metrics into a 0.0 - 1.0 bounded index via min-max scaling.
        Implements Dalio's multi-determinant equal weighting matrix strategy.
        """
        processed = df.copy()
        target_metrics = ['GDP_Share', 'Trade_Share', 'Education_Exp', 'R_D_Spend', 'Military_Exp', 'Debt_To_GDP']
        
        for metric in target_metrics:
            if metric in processed.columns:
                min_v = processed[metric].min()
                max_v = processed[metric].max()
                if max_v != min_v:
                    if metric == 'Debt_To_GDP':
                        processed[f'{metric}_Score'] = 1.0 - ((processed[metric] - min_v) / (max_v - min_v))
                    else:
                        processed[f'{metric}_Score'] = (processed[metric] - min_v) / (max_v - min_v)
                else:
                    processed[f'{metric}_Score'] = 0.5
        
        score_cols = [f'{m}_Score' for m in target_metrics if f'{m}_Score' in processed.columns]
        processed['Dalio_Power_Index'] = processed[score_cols].mean(axis=1)
        return processed

    @staticmethod
    def classify_lifecycle_stage(row: pd.Series) -> str:
        """
        Algorithmic heuristic map tracking the 6 Archetypal Stages of Great Empires.
        """
        debt = row.get('Debt_To_GDP', 0)
        mil = row.get('Military_Exp', 0)
        
        debt = 0 if np.isnan(debt) else debt
        mil = 0 if np.isnan(mil) else mil

        if debt > 115.0 and mil > 3.0:
            return "Stage 5: Financial Distress & Strategic Overextension"
        elif debt > 90.0:
            return "Stage 4: Height of Excesses, High Consumption & Leverage"
        elif debt < 50.0:
            return "Stage 1-2: Emerging Growth & System Institutional Building"
        else:
            return "Stage 3: Peak Stability, Strong Productivity & Peace"
