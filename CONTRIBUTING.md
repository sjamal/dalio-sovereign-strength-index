# Contribution Guidelines

We welcome contributions to `dalio-sovereign-strength-index` from researchers and analysts.

## Branching Methodology

*   `main`: Holds the stable production-ready code footprint. Direct commits are restricted.
*   `develop`: The central staging integration branch. All active feature developments merge here first.

## Workflow Mechanics

1. **Fork the Repository**: Create an isolated personal copy of this tracking engine workspace.
2. **Isolate Feature Scopes**: Cut a new branch out from the current `develop` stem:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```
3. **Assert Code Validation Quality**: Ensure your additions pass the complete testing array without terminal alerts:
   ```bash
   export PYTHONPATH=src
   pytest tests
   ```
4. **Submit a Pull Request (PR)**: Target your code directly toward the upstream `develop` branch. Ensure the PR is linked to an active issue tracker item before requesting an architectural review merge pass.
