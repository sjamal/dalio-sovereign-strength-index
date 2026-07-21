"""
Chaos Engineering Validation Suite.
Asserts system resilience against corrupted schemas and missing data parameters.
"""
import pytest
import pandas as pd
import numpy as np
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

def test_calculation_loop_resilience_to_null_metrics():
    """Asserts engine calculates power indices safely even when critical fields are NaN."""
    engine = DalioAnalysisEngine()
    
    # Simulate a heavily corrupted API response payload missing data fields
    corrupted_records = [
        {'year': 2025, 'Country': 'US', 'GDP_Share': np.nan, 'Trade_Share': 10.0, 'Debt_To_GDP': np.nan},
        {'year': 2025, 'Country': 'CN', 'GDP_Share': 18.0, 'Trade_Share': np.nan, 'Debt_To_GDP': 75.0}
    ]
    df = pd.DataFrame(corrupted_records)
    
    # System check: Execution must pass smoothly without throwing an exception
    try:
        scored_df = engine.calculate_power_index(df)
        assert 'Dalio_Power_Index' in scored_df.columns
        # Missing values must be backfilled or evaluated gracefully
        assert not scored_df['Dalio_Power_Index'].isna().any()
    except Exception as e:
        pytest.fail(f"Engine failed under null metric injection: {e}")

def test_engine_graceful_recovery_on_malformed_datatypes():
    """Asserts engine treats invalid metadata objects safely during lifecycle checks."""
    engine = DalioAnalysisEngine()
    
    # Inject corrupted strings into fields where numbers are explicitly expected
    malformed_row = pd.Series({
        'Debt_To_GDP': 'CRITICAL_HIGH_DATA_FAULT',
        'Military_Exp': 'MALFORMED_STRING_FIELD'
    })
    
    # Engine execution must catch the typing fault and drop to a standard stable stage status fallback
    assigned_stage = engine.classify_lifecycle_stage(malformed_row)
    assert isinstance(assigned_stage, str)
    assert "Stage" in assigned_stage
