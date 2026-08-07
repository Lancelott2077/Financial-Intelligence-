"""
config/settings.py — Central application configuration via Pydantic-Settings.

Reads values from environment variables and the .env file.
All configuration is centralised here — never read os.environ directly
in application code.

TODO: Add any additional configuration fields as the project evolves.
"""

from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application-wide settings loaded from environment / .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ──────────────────────────────────────────────────────────
    app_env: str = Field(default="development", description="Runtime environment.")
    app_host: str = Field(default="0.0.0.0", description="Bind host.")
    app_port: int = Field(default=8000, description="Bind port.")
    app_debug: bool = Field(default=True, description="Enable debug mode.")

    # ── CORS ─────────────────────────────────────────────────────────────────
    cors_origins: List[str] = Field(
        default=["http://localhost:3000"],
        description="Allowed CORS origins.",
    )

    # ── Database ─────────────────────────────────────────────────────────────
    database_url: str = Field(
        default="sqlite:///./financial_intelligence.db",
        description="SQLAlchemy database URL.",
    )

    # ── Gemini AI ─────────────────────────────────────────────────────────────
    gemini_api_key: str = Field(default="", description="Google Gemini API key.")
    gemini_model: str = Field(
        default="gemini-1.5-pro", description="Gemini model identifier."
    )

    # ── Logging ──────────────────────────────────────────────────────────────
    log_level: str = Field(default="INFO", description="Logging level.")
    log_format: str = Field(default="json", description="Log format (json | text).")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings singleton."""
    return Settings()
