"""utils/id_utils.py — UUID generation and validation helpers."""

from __future__ import annotations

import uuid


def generate_id() -> str:
    """Generate a new UUID4 as a string."""
    return str(uuid.uuid4())


def is_valid_uuid(value: str) -> bool:
    """
    Return True if value is a valid UUID string.

    TODO: Implement using uuid.UUID().
    """
    raise NotImplementedError("is_valid_uuid not implemented.")
