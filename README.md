# 📈 Sovereign Strength Index Engine (`world-order-dynamics`)
[![License: MIT](https://shields.io)](https://opensource.org)
[![CI Pipeline](https://github.com)](https://github.com)

An enterprise-grade quantitative macroeconomic simulation framework implementing the great empire lifecycle matrices from Ray Dalio's *\"Principles for Dealing with the Changing World Order\"* and the demographic workforce contraction variables from Peter Zeihan's models.

The core architecture is strictly decoupled, allowing independent ingestion data engines to feed a type-safe mathematical calculation matrix, exposed simultaneously across three presentation layers: a traditional FastAPI REST layer, a visual Streamlit web dashboard, and an advanced Model Context Protocol (MCP) server optimized for autonomous AI Agents.

---

## 🖥️ Streamlit Interface Dashboard Blueprint

Below is a visual schematic map of the interactive frontend panel (`src/dalio_sovereign_strength_index/app_ui.py`) rendering your comparative superpower analytics tracks:

```text
+---------------------------------------------------------------------------------------+

| 🧠 Sovereign Strength Index Dashboard                                                 |
| Ingesting real-time multi-determinant arrays across global sovereign regimes          |
+---------------------------------------------------------------------------------------+

| [ SIDEBAR CONTROLS ]        |  🇺🇸 United States Matrix     |  🇨🇳 China Matrix         |
|                             |  Total Power: [ 0.667 ]     |  Total Power: [ 0.246 ]  |
|  Timeline Focus             |  +------------------------+ |  +---------------------+ |
|  [ Start: 2018 | End: 2025 ]|  | State: Stage 5 (Blue)  | |  | State: Stage 4 (Red)| |
|                             |  +------------------------+ |  +---------------------+ |
|  🇺🇸 US Crisis Shocks       |  - Debt-to-GDP: 128.5%     |  - Debt-to-GDP: 88.3%   |
|  - Debt Shock:   [ +15% ]   |  - Mil. Budget: 3.40%      |  - Mil. Budget: 1.70%   |
|  - Mil. Budget:  [ +0.0% ]  |                             |                          |
|                             |  ----------------------------------------------------- |
|  🇨🇳 China Crisis Shocks    |  [ Relative Trajectory Chart Trend Plots Lines ]       |
|  - Debt Shock:   [ +0.0% ]  |  1.0 |                    /--[China (Red)]             |
|  - Mil. Budget:  [ +1.5% ]  |  0.5 |  \----------------                              |
|                             |  0.0 +-----------------------[US (Blue)]----           |
|                             |        2018      2020      2022      2024    2026      |
+---------------------------------------------------------------------------------------+

| ⚙️ System Performance and Diagnostic Operations                                       |
|  +-------------------------------------+ +------------------------------------------+ |
|  | Tab 1: Superpower Macro Trends [ACT] | | Tab 2: MCP Server Stream Performance     | |
|  +-------------------------------------+ +------------------------------------------+ |
|  | - Displays raw numeric matrices tables tracking combined data arrays from APIs.   | |
|  +----------------------------------------------------------------------------------+ |
```

---

## 🗂️ Core Domain Layout

```text
├── .github/workflows/
│   └── ci_pipeline.yml         # GitHub Actions Node 24/Ubuntu Native validation track
├── docs/
│   ├── adr/                    # Architecture Decision Records logs (ADR 0001 - 0003)
│   └── macro_summary_report.txt# Auto-compiled analytics reporting text files
├── scripts/
│   ├── mcp_harness.py          # Isolated local AI simulation payload checker
│   └── mcp_bench_reporter.py   # High-speed JSON-RPC benchmark generator script
├── src/dalio_sovereign_strength_index/
│   ├── engines/                # Modular alternative data connector classes
│   │   ├── base_engine.py      # Abstract execution interface contract
│   │   ├── engine_worldbank.py # World Bank explicit sub-module ingestion pipeline
│   │   ├── engine_fred.py      # Sovereign leverage evaluation curves proxy
│   │   ├── engine_demographics.py # Peter Zeihan workforce contraction score model
│   │   └── engine_reserves.py   # Global central bank allocation metrics matrix
│   ├── engine.py               # Core quantitative logic & stage triggers
│   ├── pipeline.py             # Central multi-source data merge orchestrator
│   ├── app_fastapi.py          # REST API Microservice presentation tier
│   ├── app_mcp.py              # Model Context Protocol standard stream gateway
│   └── app_ui.py               # Visual analytics dashboard layout (Symmetric colors)
└── tests/
    ├── test_engine.py          # Normalization bounds verification tests
    └── test_chaos.py           # Defensive type-coercion validation suites
```

---

## ⚙️ Quickstart Operations Guide

### 1. Environment Assembly
Initialize an isolated virtual workspace environment and download dependencies natively:
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest streamlit
```

### 2. Verify System Integrity
Execute your complete calculation and chaos-engineering test suites locally:
```bash
export PYTHONPATH=src
pytest tests
```

### 3. Launch the Presentations Channels
*   **Run the Interactive Visual Frontend Dashboard**:
    ```bash
    streamlit run src/dalio_sovereign_strength_index/app_ui.py
    ```
*   **Activate local REST HTTP Web Services**:
    ```bash
    uvicorn dalio_sovereign_strength_index.app_fastapi:app --reload --port 8000
    ```

---

## 🤝 Branch Strategy & Open Source Contributions

We operate a strict, professional branch lifecycle model to ensure high codebase quality. Please see `CONTRIBUTING.md` for our full onboarding guidelines.

*   `main`: Houses our immutable, stable, production-ready release footprint.
*   `develop`: The central staging integration branch. All custom feature tasks merge here via Pull Requests (PRs) after clearing active unit test assertions.

---

## 🏛️ Scholastic Appendix: The Macro Reality of Dalio's Big Cycles

Users reviewing standard historical timelines will observe that calculated lifecycle status bounds remain fixed across standard horizons (United States locked in Stage 5, China locked in Stage 4). This behavior is theoretically deliberate.

In Ray Dalio's historical framework, an empire's full "Big Cycle" transpires over **200 to 250 years**. Short-term windows represent distinct frames at the tail-end of a multi-century regime.

*   **The United States (Stage 5)** represents an empire experiencing high financial leverage coupled with global strategic overextension. The engine locks it here due to structural Debt-to-GDP parameters exceeding 115% combined with significant hard-power military commitments.
*   **China (Stage 4)** represents the ascendant competitor empire. It has advanced past productivity rebuilding (Stage 3) into a phase of rapid infrastructure accumulation and leverage growth, positioning it firmly within the "Height of Excesses" parameters.
