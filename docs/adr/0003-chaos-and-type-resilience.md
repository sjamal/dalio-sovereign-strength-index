# ADR 0003: Defensive Type-Coercion for API Fault Tolerance

## Context and Problem Statement
Chaos engineering validation scans revealed that third-party data providers (like the World Bank or FRED) can return inconsistent metadata objects, empty strings, or text string descriptors rather than clean floating-point numbers. This caused mathematical processing operations inside `engine.py` to fail on `TypeError` bugs during runtime execution passes.

## Decision Outcome
We implemented a strict defensive type-coercion layer inside the core calculation loops of `DalioAnalysisEngine`. 

All incoming parameters pass through `pd.to_numeric(..., errors='coerce')` filters. This automatically converts text faults or empty responses into valid `NaN` properties. The model then applies a stable fallback index value (`0.5`) to preserve data integrity and keep background system threads running smoothly.
