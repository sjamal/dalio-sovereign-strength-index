# ADR 0001: Concurrent Architectural Support for REST (FastAPI) and MCP

## Context and Problem Statement
The platform targets two distinct user groups: traditional macro researchers who need access via analytical web dashboards, and AI agents/LLM contexts requiring dynamic tools to pull quantitative data on demand.

## Considered Options
1. **REST API Only**: Standard, accessible, but requires complex parsing structures for LLMs.
2. **MCP Server Only**: Highly optimized for AI integration, but unusable by traditional frontend scripts or dashboards.
3. **Decoupled Engine with Dual Presentation Adapters**: Isolates the data pipelines and mathematical formulas from the delivery protocol layer.

## Decision Outcome
Chosen Option: **Option 3**. By keeping `pipeline.py` and `engine.py` completely protocol-agnostic, we can run FastAPI and MCP servers simultaneously over the same logic without duplicating codebase operations.
