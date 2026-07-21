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

## Macro System Diagnostic Rule Triggers

*   **Stage 5: Strategic Overextension Indicator**: Triggered if national sovereign `Debt_To_GDP` exceeds 115% while `Military_Exp` scales past 3.0% of GDP. Matches the late-peak profile of a reigning global hegemon.
*   **Stage 4: Height of Excesses Indicator**: Triggered if sovereign `Debt_To_GDP` scales past 50% to 90% without crossing the hyper-extended global military budget requirements. Matches the profile of an ascendant competitor empire.

