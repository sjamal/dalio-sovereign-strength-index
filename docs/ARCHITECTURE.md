# Architectural Specification Log

## Data Pipeline Logic Flow Mapping
[ Alternative Engines Hub (World Bank / FRED) ]
│
▼ (Raw Matrix Layout)
[ Dalio Analysis Engine Matrix ]
│
┌─────────────┴─────────────┐
▼                           ▼
[ FastAPI Gateways ]     [ MCP Protocol Streams ]
(JSON HTTP REST)         (JSON-RPC Local Agents)

## Underlying Indicator Matrix Weights

| Core Indicator | Ingestion Engine | Vector Weight Modifier | Target Action |
| :--- | :--- | :--- | :--- |
| **GDP_Share** | World Bank API | Equal In-Distribution | Positive Strength Scale |
| **Trade_Share** | World Bank API | Equal In-Distribution | Positive Strength Scale |
| **Debt_To_GDP** | FRED Proxy Hub | Inverse Deductible Array | Negative Risk Penalty |
| **Military_Exp** | World Bank API | Threshold Check Heuristic | Stage Lifecycle Trigger |