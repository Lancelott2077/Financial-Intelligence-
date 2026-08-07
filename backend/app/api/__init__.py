"""
api package — FastAPI route handlers.

Each module corresponds to one functional area of the platform.
Routers are registered in app/main.py.

Modules:
    upload          POST /upload — CSV file ingestion endpoint.
    snapshot        GET  /snapshot/{session_id} — Financial snapshot.
    behaviours      GET  /behaviours/{session_id} — Detected behaviours.
    savings         GET  /savings/{session_id} — Savings opportunities.
    simulation      POST /simulation — Counterfactual simulation.
    coach           POST /coach/chat — AI financial coach conversation.
    plan            GET  /plan/{session_id} — Action plan.
"""
