"""
config/database.py — SQLAlchemy engine, session factory, and base model.

TODO: Implement async session support via aiosqlite.
TODO: Add connection pool configuration.
TODO: Implement database migration strategy (Alembic).
"""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from typing import Generator

from app.config.settings import get_settings


class Base(DeclarativeBase):
    """Declarative base class for all ORM models."""

    pass


def _create_engine():
    """Create the SQLAlchemy engine from settings."""
    settings = get_settings()
    # TODO: Replace connect_args with proper async driver for production.
    return create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False},  # SQLite only
        echo=settings.app_debug,
    )


engine = _create_engine()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that yields a database session.

    Usage::

        @router.get("/example")
        def example(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """
    Create all database tables defined in ORM models.

    TODO: Replace with Alembic migrations for production.
    """
    # Import all models here so Base.metadata knows about them.
    # from app.models import transaction, session, behaviour, plan  # noqa: F401
    Base.metadata.create_all(bind=engine)
