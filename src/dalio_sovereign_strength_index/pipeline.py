"""
Central Ingestion Pipeline Orchestrator.
Loops through decoupled alternative modules to build an aggregate analytical table.
"""
import pandas as pd
from dalio_sovereign_strength_index.engines.engine_worldbank import WorldBankDataEngine
from dalio_sovereign_strength_index.engines.engine_fred import FredDataEngine

class MacroDataPipeline:
    def __init__(self):
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
                # Force columns to string types before merging to ensure string keys line up cleanly
                master_df['year'] = master_df['year'].astype(str)
                master_df['Country'] = master_df['Country'].astype(str)
                engine_df['year'] = engine_df['year'].astype(str)
                engine_df['Country'] = engine_df['Country'].astype(str)
                
                master_df = pd.merge(master_df, engine_df, on=['year', 'Country'], how='outer')
                
        # FIX: Strip multi-index object artifacts and force structural keys back to numeric metrics
        master_df['year'] = pd.to_numeric(master_df['year'], errors='coerce').astype(int)
        master_df['Country'] = master_df['Country'].astype(str)
        
        # Sort values precisely before applying line interpolation mechanics
        master_df = master_df.sort_values(['Country', 'year']).reset_index(drop=True)
        
        # Isolate index keys from numeric interpolation data matrices
        numeric_cols = master_df.select_dtypes(include=['number']).columns
        master_df[numeric_cols] = master_df[numeric_cols].interpolate(method='linear').fillna(0.5)
        
        return master_df
