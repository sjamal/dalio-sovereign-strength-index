# Operations Reference Manual

## Environment Assembly

1. **Clone your active workspace branch locally**:
   ```bash
   git clone https://github.com
   cd dalio-sovereign-strength-index
   ```

2. **Initialize isolated dependency environments**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install pytest streamlit
   ```

## Component Activation Routines

### Execution Pass Unit Testing Intercepts
```bash
export PYTHONPATH=src
pytest tests
```

### Launch Interactive Graphics Panel via Streamlit
```bash
streamlit run src/dalio_sovereign_strength_index/app_ui.py
```

### Run Web REST Service Gateway App
```bash
uvicorn dalio_sovereign_strength_index.app_fastapi:app --reload --port 8000
```
