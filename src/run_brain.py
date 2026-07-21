"""
Unified Local Pipeline Script Runner.
Executes an end-to-end integration pass and drops a data layout report to the console.
"""
from dalio_sovereign_strength_index.pipeline import MacroDataPipeline
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

def execute_complete_pass():
    print("================================================================")
    print("🧠 RUNNING UNIFIED SOVEREIGN STRENGTH INDEX PIPELINE PASSTHROUGH")
    print("================================================================\n")
    
    print("[Pipeline] Sourcing indicators across alternative engine hubs...")
    pipeline = MacroDataPipeline()
    raw_matrix = pipeline.execute_pipeline(start_yr=2020, end_yr=2025)
    print(f"-> Matrix constructed successfully. Synced {len(raw_matrix)} unique time records.\n")
    
    print("[Engine] Processing multi-determinant min-max normalization arrays...")
    engine = DalioAnalysisEngine()
    scored_matrix = engine.calculate_powe    scored_matrix = engine.caprint("[Engine] Evaluating sovereign locations along archetypal 6-stage models...")
    scored_matrix['Assigned_Lifecycle_Stage'] = scored_matrix.apply(engine.classify_lifecycle_stage, axis=1)
    
    prin    prin    prin    prin    prin    prin    prin    prin   ---------")
    target_columns = ['year',    target_columns = ['year',    target_columns = ['year',    target_coluored_matrix[target_columns].tail(6).to_string(index=False))
    print("--------------    print("--------------    print("--------------    print("--------line compilation run finished without terminal faults.")

if __name__ == "__main__":
    execute_complete_pass()
