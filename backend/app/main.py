"""
Financial Intelligence — FastAPI Application Entry Point.

This module bootstraps the FastAPI application, registers middleware,
mounts all API routers, and configures lifecycle events.

TODO: Implement startup/shutdown lifecycle events.
TODO: Wire all API routers once implemented.
TODO: Add request-ID middleware.
TODO: Add rate limiting middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings
from app.api import upload, plan

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    settings = get_settings()

    app = FastAPI(
        title="Financial Intelligence API",
        description=(
            "AI-powered behavioural finance platform — analyses spending patterns, "
            "detects cognitive biases, and delivers personalised financial coaching."
        ),
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # ── CORS ────────────────────────────────────────────────────────────────
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── Routers ─────────────────────────────────────────────────────────────
    app.include_router(
        upload.router,
        prefix="/api/v1/upload",
        tags=["Upload"],
    )
    app.include_router(
        plan.router,
        prefix="/api/v1/plan",
        tags=["Plan"],
    )

    # ── Health check ─────────────────────────────────────────────────────────
    @app.get("/health", tags=["Health"])
    async def health_check() -> dict:
        """Return API health status."""
        return {"status": "ok", "version": "0.1.0"}

    return app


# ---------------------------------------------------------------------------
# Application instance (imported by uvicorn)
# ---------------------------------------------------------------------------

app = create_app()
