"""
config/logging.py — Application-wide Loguru logging configuration.

TODO: Add JSON sink for structured logging in production.
TODO: Integrate with cloud logging provider (e.g., Google Cloud Logging).
"""

from __future__ import annotations

import sys
from loguru import logger

from app.config.settings import get_settings


def configure_logging() -> None:
    """Configure Loguru logger based on application settings."""
    settings = get_settings()

    logger.remove()  # Remove default handler

    # TODO: Implement JSON format sink for production environments.
    logger.add(
        sys.stdout,
        level=settings.log_level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> — "
            "<level>{message}</level>"
        ),
        colorize=True,
    )


__all__ = ["configure_logging", "logger"]
