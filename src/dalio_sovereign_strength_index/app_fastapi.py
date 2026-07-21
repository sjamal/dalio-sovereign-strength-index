"""
REST API Microservice Presentation Layer.
Exposes calculation matrices and cycle gauges via JSON payloads over HTTP.
"""
from fastapi import FastAPI, Query
from dalio_sovereign_strength_index.pipeline import MacroDataPipeline
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

app = FastAPI(
    title="Dalio Sovereign Strength Index Analytical API",
    description="REST endpoint layer outputting macro indexes and lifecycle tests.",
    version="1.0.0"
)

@app.get("/api/v1/analyze")
def get_macro_analysis(start_year: int = Query(2018, ge=2000), end_year: int = Query(2025, le=2026)):
    """Triggers alternative data pipelines and returns calculated power index vectors."""
    pipeline = MacroDataPipeline()
    engine = DalioAnalysisEngine()
    
    raw_matrix = pipeline.execute_pipeline(start_yr=start_year, end_yr=end_year)
    scored_matrix = engine.calculate_power_index(raw_matrix)
    
    scored_matrix['Assigned_Stage'] = scored_matrix.apply(engine.classify_lifecycle_stage, axis=1)
    return scored_matrix.to_dict(orient="records")
