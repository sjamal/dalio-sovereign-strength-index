"""
Model Context Protocol (MCP) Server Interface.
Exposes sovereign strength metrics and dynamic parameter tracking over standard IO.
"""
import sys
import json
import pandas as pd
from dalio_sovereign_strength_index.pipeline import MacroDataPipeline
from dalio_sovereign_strength_index.engine import DalioAnalysisEngine

def process_rpc_payload(raw_line: str) -> str:
    """
    Evaluates JSON-RPC schema calls sent from an LLM runtime environment.
    Supports historical windows and customizable debt penalty modifiers.
    """
    try:
        req = json.loads(raw_line)
        method = req.get("method")
        req_id = req.get("id")
        
        # 1. Handle Tool Discovery requests from the AI Agent
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [{
                        "name": "backtest_sovereign_strength",
                        "description": "Calculates sovereign strength indices using dynamic evaluation windows and asset penalty configurations.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "start_year": {"type": "integer", "minimum": 2000, "default": 2018},
                                "end_year": {"type": "integer", "maximum": 2026, "default": 2025},
                                "debt_weight_penalty": {"type": "number", "minimum": 0.0, "maximum": 2.0, "description": "Custom multiplier penalty for sovereign debt risk indices."}
                            },
                            "required": ["start_year", "end_year"]
                        }
                    }]
                }
            })
            
        # 2. Handle Explicit Tool Execution requests triggered by the AI
        elif method == "tools/call":
            arguments = req.get("params", {}).get("arguments", {})
            start_yr = int(arguments.get("start_year", 2018))
            end_yr = int(arguments.get("end_year", 2025))
            penalty = float(arguments.get("debt_weight_penalty", 1.0))
            
            # Execute underlying multi-source pipeline and calculation matrices
            pipeline = MacroDataPipeline()
            engine = DalioAnalysisEngine()
            
            raw_matrix = pipeline.execute_pipeline(start_yr, end_yr)
            scored = engine.calculate_power_index(raw_matrix)
            
            # Dynamically apply custom parameter scaling if requested by the LLM
            if 'Debt_To_GDP_Score' in scored.columns and penalty != 1.0:
                scored['Dalio_Power_Index'] = scored['Dalio_Power_Index'] * (scored['Debt_To_GDP_Score'] * penalty)
                
            scored['Stage_Status'] = scored.apply(engine.classify_lifecycle_stage, axis=1)
            
            # Return standardized payload to the standard output buffer channel
            return json.dumps({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{
                        "type": "text", 
                        "text": scored[['year', 'Country', 'Dalio_Power_Index', 'Stage_Status']].to_json(orient="records")
                    }]
                }
            })
            
        return json.dumps({"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}})
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}})

def main():
    """Main input loop handling direct standard IO stream routing loops."""
    for line in sys.stdin:
        if not line.strip():
            continue
        response = process_rpc_payload(line)
        sys.stdout.write(response + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
