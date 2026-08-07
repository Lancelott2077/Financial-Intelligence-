"""
ai/response_parser.py — Parses and validates Gemini JSON responses.

Handles the extraction and validation of structured data from
Gemini text responses.

TODO: Implement JSON extraction from markdown code fences.
TODO: Implement schema validation of parsed responses.
TODO: Handle partial JSON and retry logic.
"""

from __future__ import annotations

import json
import re


class ResponseParser:
    """Parses structured data from Gemini AI responses."""

    def extract_json(self, response_text: str) -> dict | list:
        """
        Extract JSON from a Gemini response string.

        Handles both raw JSON and JSON wrapped in markdown code fences.

        TODO: Use regex to extract JSON from ```json ... ``` blocks.
        TODO: Fallback to attempting raw json.loads().
        TODO: Raise ValueError with context if JSON is invalid.
        """
        raise NotImplementedError("ResponseParser.extract_json not implemented.")

    def extract_categories(self, response_text: str) -> list[str]:
        """
        Extract a list of category strings from a categorisation response.

        TODO: Call extract_json and validate against expected category list.
        """
        raise NotImplementedError("ResponseParser.extract_categories not implemented.")
