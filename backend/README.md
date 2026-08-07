# Backend — Financial Intelligence Platform

## Overview

FastAPI backend for the Financial Intelligence behavioural finance AI platform.

---

## Structure

```
app/
├── main.py               # Application entry point & middleware
├── api/                  # Route handlers (controllers)
├── config/               # Settings & environment loading
├── models/               # SQLAlchemy ORM models
├── schemas/              # Pydantic request/response schemas
├── services/             # Business logic layer
├── processing/           # CSV ingestion & data pipeline
├── features/             # Feature extraction from transactions
├── behaviours/           # Behavioural bias detectors
├── evidence/             # Evidence collection for detected biases
├── decisions/            # Decision / rule engine
├── simulation/           # Counterfactual simulation engine
├── ai/                   # Gemini AI integration
├── orchestration/        # Pipeline orchestration & job management
└── utils/                # Shared utilities
```

---

## Running

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs`.

---

*Placeholder backend — no business logic implemented.*
