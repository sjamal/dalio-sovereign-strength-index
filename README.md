# 📈 Sovereign Strength Index Engine (`world-order-dynamics`)
[![License: MIT](https://shields.ioLicense-MIT-blue)](https://github.com/sjamal/dalio-sovereign-strength-index/blob/main/LICENSE)
[![CI Pipeline](https://github.com/sjamal/dalio-sovereign-strength-index/actions/workflows/ci_pipeline.yml/badge.svg)](https://github.com/sjamal/dalio-sovereign-strength-index/actions/workflows/ci_pipeline.yml)

An enterprise-grade quantitative macroeconomic simulation framework implementing the great empire lifecycle matrices from Ray Dalio's *\"Principles for Dealing with the Changing World Order\"* and the demographic workforce contraction variables from Peter Zeihan's models.

The core architecture is strictly decoupled, allowing independent ingestion data engines to feed a type-safe mathematical calculation matrix, exposed simultaneously across three presentation layers: a traditional FastAPI REST layer, a visual Streamlit web dashboard, and an advanced Model Context Protocol (MCP) server optimized for autonomous AI Agents.

---

## 🖥️ Streamlit Interface Dashboard Blueprint

Below is the layout specification mapping the dashboard interface (`src/dalio_sovereign_strength_index/app_ui.py`). It shows symmetric structural metrics panel views and side control sliders:

| 🎛️ Left Sidebar Controls | 🇺🇸 United States State Matrix (Blue Banner) | 🇨🇳 China State Matrix (Red Banner) |
| :--- | :--- | :--- |
| **Timeline Focus**<br>• Start Horizon Year (Slider)<br>• End Horizon Year (Slider) | **Total Strength Index Score**<br>• Dynamic Float Output Metric | **Total Strength Index Score**<br>• Dynamic Float Output Metric |
| **🇺🇸 US Crisis Shocks**<br>• US Debt Shock Addition (%)<br>• US Military Alteration (% GDP) | **Calculated Lifecycle State**<br>• Text Status: e.g., Stage 5 Overextension | **Calculated Lifecycle State**<br>• Text Status: e.g., Stage 4 Height of Excesses |
| **🇨🇳 China Crisis Shocks**<br>• China Debt Shock Addition (%)<br>• China Military Alteration (% GDP) | **Telemetry Indicators Breakdown**<br>• Debt to GDP Ratio (%)<br>• Military Budget (% GDP) | **Telemetry Indicators Breakdown**<br>• Debt to GDP Ratio (%)<br>• Military Budget (% GDP) |
| | **Relative Trajectory Trend Line Chart**<br>• Blue Line: United States Trajectory | **Relative Trajectory Trend Line Chart**<br>• Red Line: China Trajectory |

### ⚙️ System Performance and Diagnostic Operations Tabs
*   **Tab 1: Superpower Macro Trends (Active View)**: Renders the active multi-variable pandas tracking data matrix table data directly on the screen layout.
*   **Tab 2: MCP Server Automation Performance**: Renders the historical JSON-RPC looping speeds data arrays line chart dynamically pulling from the local `.csv` metrics sheet.

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
Execute the complete calculation and chaos-engineering test suites locally:
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

A strict, professional branch lifecycle model is operated to ensure high codebase quality. Please see `CONTRIBUTING.md` for full onboarding guidelines.

*   `main`: Houses the immutable, stable, production-ready release footprint.
*   `develop`: The central staging integration branch. All feature tasks merge here via Pull Requests (PRs) after clearing active unit test assertions.

---

## 🏛️ Scholastic Appendix: The Macro Reality of Dalio's Big Cycles

Reviewing standard historical timelines demonstrates that calculated lifecycle status bounds remain fixed across standard horizons (United States locked in Stage 5, China locked in Stage 4). This behavior is mathematically deliberate.

In Ray Dalio's historical framework, an empire's full "Big Cycle" transpires over **200 to 250 years**. Short-term windows represent distinct frames at the tail-end of a multi-century regime.

*   **The United States (Stage 5)** represents an empire experiencing high financial leverage coupled with global strategic overextension. The engine locks the status here due to structural Debt-to-GDP parameters exceeding 115% combined with significant hard-power military commitments.
*   **China (Stage 4)** represents the ascendant competitor empire. Advancement has passed productivity rebuilding (Stage 3) into a phase of rapid infrastructure accumulation and leverage growth, positioning the asset firmly within the "Height of Excesses" parameters.
