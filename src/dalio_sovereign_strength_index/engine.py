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
                # Force columns to numeric values; bad text turns into NaN values
                processed[metric] = pd.to_numeric(processed[metric], errors='coerce')
                
                min_v = processed[metric].min()
                max_v = processed[metric].max()
                
                # Backfill NaN metrics with a conservative neutral score (0.5)
                if pd.isna(min_v) or pd.isna(max_v) or max_v == min_v:
                    processed[f'{metric}_Score'] = 0.5
                else:
                    if metric == 'Debt_To_GDP':
                        processed[f'{metric}_Score'] = 1.0 - ((processed[metric] - min_v) / (max_v - min_v))
                    else:
                        processed[f'{metric}_Score'] = (processed[metric] - min_v) / (max_v - min_v)
                
                # Clean up any final row-level NaNs inside individual score columns
                processed[f'{metric}_Score'] = processed[f'{metric}_Score'].fillna(0.5)
        
        score_cols = [f'{m}_Score' for m in target_metrics if f'{m}_Score' in processed.columns]
        processed['Dalio_Power_Index'] = processed[score_cols].mean(axis=1)
        return processed

    @staticmethod
    def classify_lifecycle_stage(row: pd.Series) -> str:
        """
        Algorithmic heuristic map tracking the 6 Archetypal Stages of Great Empires.
        Safe against bad metadata objects and invalid text strings.
        """
        # Safely convert inputs to numeric parameters; strings turn into NaN
        debt_raw = pd.to_numeric(row.get('Debt_To_GDP', 0), errors='coerce')
        mil_raw = pd.to_numeric(row.get('Military_Exp', 0), errors='coerce')
        
        # If the input is NaN, fall back to a safe default of 0
        debt = 0.0 if pd.isna(debt_raw) else float(debt_raw)
        mil = 0.0 if pd.isna(mil_raw) else float(mil_raw)

        if debt > 115.0 and mil > 3.0:
            return "Stage 5: Financial Distress & Strategic Overextension"
        elif debt > 90.0:
            return "Stage 4: Height of Excesses, High Consumption & Leverage"
        elif debt < 50.0:
            return "Stage 1-2: Emerging Growth & System Institutional Building"
        else:
            return "Stage 3: Peak Stability, Strong Productivity & Peace"
