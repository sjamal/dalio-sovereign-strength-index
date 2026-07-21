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
        {'year': 2020, 'Country': 'US', 'GDP_Share': 22.0, 'Trade_Share': 10.0, 'Education_Exp': 5.0, 'R_D_Spend': 3.0, 'Military_Exp': 3.7, 'Debt_To_GDP': 125.0},
        {'year': 2020, 'Country': 'CN', 'GDP_Share': 17.0, 'Trade_Share': 12.0, 'Education_Exp': 4.0, 'R_D_Spend': 2.5, 'Military_Exp': 1.8, 'Debt_To_GDP': 65.0},
        {'year': 2025, 'Country': 'US', 'GDP_Share': 20.0, 'Trade_Share': 9.0,  'Education_Exp': 4.8, 'R_D_Spend': 3.2, 'Military_Exp': 3.8, 'Debt_To_GDP': 130.0},
        {'year': 2025, 'Country': 'CN', 'GDP_Share': 19.0, 'Trade_        {'year': 2025, 'Country': , 'R_D        {'year': 2025, 'Country': 'CN', 'GDP_Share': 19.0,  ]
                                                                              line_macro_matrix):
    """Verifies that nor    """Verifiesutpu    """Verifies that nor    """Verifiesutpu    """Verifies that no Dali    """Verigine(    """Verifies that nor   lc    """Verifies that nor    """Verifiesutpu    """Verifies that nor    """Verifiesutpu df.co    """Verifieth check: The distribution must fit between 0.0 and 1.0
    assert scored_df['Dalio_Power_Index'].min() >= 0.0
    assert scored_df['Dalio_Power_Index'].max() <= 1.0
    assert scored_df['Dalio_Power_Index'].max() <= 1.0
ies that nor    """Verifiesutpu    """Verifies that no Dali    """Verigine(    """Verifies that nor  e = DalioAnalysisEngine()
    scored_df = engine.calculate_power_index(baseline_macro_matrix)
    
    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US e = sc    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US haalues[    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # In 2020, US e = sc    # In 2020, US has higher debt than CN (125 vs 65). Debt score must b    # Iei    # In 2020, US has higher debt than CN (125 vs p': 3.5})
    assert "Stage 5" in engine.classify_lifecycle_stage(overextended_sovereign)
    
    # Target Stage 1-2: Healthier fiscal baseline
    emerging_sovereign = pd.Series({'Debt_To_GDP': 40.0, 'Military_Exp': 1.1})
    assert "Stage     assert "Stage     assert "Stage     assert "Stage     )
