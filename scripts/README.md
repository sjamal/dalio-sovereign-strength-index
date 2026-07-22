# ⚙️ Automation Scripts Directory

This directory contains standalone execution utilities and benchmarking harnesses designed to interact with the core engine presentation layers.

## Component Execution

### 1. Programmatic AI Agent Simulation (`mcp_harness.py`)
Simulates an LLM agent sending standard JSON-RPC packets directly down the Model Context Protocol (MCP) server input stream:
```bash
export PYTHONPATH=src
python scripts/mcp_harness.py
```

### 2. Performance Profiler & Report Generator (`mcp_bench_reporter.py`)
Executes 50 continuous processing loops over the MCP channel, records processing speeds, and auto-compiles an analytical summary report:
```bash
export PYTHONPATH=src
python scripts/mcp_bench_reporter.py
```
