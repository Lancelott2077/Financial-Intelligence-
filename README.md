# Financial Intelligence — Behavioural Finance AI Platform

> **Hackathon Project** — Production-ready scaffold. Business logic will be implemented incrementally.

## Overview

An AI-powered personal finance platform that analyses spending behaviour, detects cognitive biases, generates counterfactual simulations, and delivers personalised financial coaching via a conversational Gemini-powered agent.

---

## Project Structure

```
Financial-Intelligence-/
├── backend/          # FastAPI Python backend
├── frontend/         # Next.js TypeScript frontend
├── datasets/         # Sample CSV datasets (not committed)
├── docs/             # Engineering documentation
├── prompts/          # Gemini prompt templates
├── .env.example      # Environment variable template
└── .gitignore
```

---

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:3000`.  
The backend API will be available at `http://localhost:8000`.  
Interactive API docs: `http://localhost:8000/docs`.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in values before running.

---

## Documentation

| Document | Purpose |
|---|---|
| `docs/architecture.md` | System architecture overview |
| `docs/api_contract.md` | REST API contract |
| `docs/schemas.md` | Data schemas & models |
| `docs/coding_guidelines.md` | Code style & conventions |
| `docs/development_plan.md` | Incremental build plan |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, React, TypeScript, Tailwind CSS, shadcn/ui, Recharts |
| Backend | FastAPI, Python 3.11+, Pydantic v2, Pandas, NumPy |
| AI | Google Gemini API |
| Database | SQLite (development) |

---

*Generated scaffold — no business logic implemented yet.*
