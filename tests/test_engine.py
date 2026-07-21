"""
Unit Validation Suite for Sovereign Strength Index Calculations.
Asserts normalization constraints, inverse debt penalties, and stage boundaries.
"""
import pytest
import pandas as pd
import numpy as np
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

@pytest.fixture
def baseline_macro_matrix():
    """Generates an isolated historical mock matrix for consistent mathematical testing."""
    records = [
        {"year": 2020, "Country": "US", "GDP_Share": 22.0, "Trade_Share": 10.0, "Education_Exp": 5.0, "R_D_Spend": 3.0, "Military_Exp": 3.7, "Debt_To_GDP": 125.0},
        {"year": 2020, "Country": "CN", "GDP_Share": 17.0, "Trade_Share": 12.0, "Education_Exp": 4.0, "R_D_Spend": 2.5, "Military_Exp": 1.8, "Debt_To_GDP": 65.0},
        {"year": 2025, "Country": "US", "GDP_Share": 20.0, "Trade_Share": 9.0,  "Education_Exp": 4.8, "R_D_Spend": 3.2, "Military_Exp": 3.8, "Debt_To_GDP": 130.0},
        {"year": 2025, "Country": "CN", "GDP_Share": 19.0, "Trade_Share": 14.0, "Education_Exp": 4.2, "R_D_Spend": 2.8, "Military_Exp": 1.9, "Debt_To_GDP": 72.0}
    ]
    return pd.DataFrame(records)

def test_power_index_scaling_and_bounds(baseline_macro_matrix):
    """Verifies that normalized power output indices remain within strictly legal 0-1 bounds."""
    engine = DalioAnalysisEngine()
    scored_df = engine.calculate_power_index(baseline_macro_matrix)
    
    assert 'Dalio_Power_Index' in scored_df.columns
    assert scored_df['Dalio_Power_Index'].min() >= 0.0
    assert scored_df['Dalio_Power_Index'].max() <= 1.0

def test_inverse_debt_scoring(baseline_macro_matrix):
    """Asserts that higher relative debt accurately penalizes a sovereign's power score."""
    engine = DalioAnalysisEngine()
    scored_df = engine.calculate_power_index(baseline_macro_matrix)
    
    us_debt_score = scored_df[(scored_df['year'] == 2020) & (scored_df['Country'] == 'US')]['Debt_To_GDP_Score'].values
    cn_debt_score = scored_df[(scored_df['year'] == 2020) & (scored_df['Country'] == 'CN')]['Debt_To_GDP_Score'].values
    
    assert us_debt_score < cn_debt_score

def test_lifecycle_stage_classification():
    """Asserts that specific macroeconomic vulnerabilities trigger the correct lifecycle stage."""
    engine = DalioAnalysisEngine()
    
    overextended_sovereign = pd.Series({'Debt_To_GDP': 120.0, 'Military_Exp': 3.5})
    assert "Stage 5" in engine.classify_lifecycle_stage(overextended_sovereign)
    
    emerging_sovereign = pd.Series({'Debt_To_GDP': 40.0, 'Military_Exp': 1.1})
    assert "Stage 1-2" in engine.classify_lifecycle_stage(emerging_sovereign)
