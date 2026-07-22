# 🧪 Validation and Verification Test Suite

This directory houses the localized testing matrices handled by the `pytest` engine framework.

## Execution Matrix

To run all integrity and chaos verification passes simultaneously, execute the following command from the project root:
```bash
export PYTHONPATH=src
pytest tests/
```

## Coverage Scopes
*   `test_engine.py`: Asserts mathematical distribution limits, scoring engine parity, and equal-weight normalization bounds.
*   `test_chaos.py`: Exercises fault-tolerance parameters by injecting malformed strings, null variables, and corrupted types to verify system resilience.
