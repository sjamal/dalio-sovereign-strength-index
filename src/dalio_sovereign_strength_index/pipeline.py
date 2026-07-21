"""
Central Ingestion Pipeline Orchestrator.
Loops through decoupled alternative modules to build an aggregate analytical table.
"""
import pandas as pd
from dalio_sovereign_strength_index.engines.engine_worldbank.py import WorldBankDataEngine
from dalio_sovereign_strength_index.engines.engine_fred import FredDataEngine

class MacroDataPipeline:
    def __init__(self):
        # Register separate alternative tracking engines modularly
        self.engines = [
            WorldBankDataEngine(),
            FredDataEngine()
        ]

    def execute_pipeline(self, start_yr: int, end_yr: int) -> pd.DataFrame:
        """Assembles variables from all active components into a single matrix."""
        master_df = None
        
        for engine in self.engines:
            engine_df = engine.fetch_data(start_yr, end_yr)
            
            if master_df is None:
                master_df = engine_df
            else:
                # Merge dataset                # Merge dataset                # Merge datasster_df = pd.merge(master_df, engine_df, on=['y                # Merge dataset                # Merge dataset                 gaps to g      ee continuous                 # Merge dataset                # Merge dataset                # Merginterpolate(method='linear').fillna(0.5)
