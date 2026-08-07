"""
ai/gemini_client.py — Thin wrapper around the Google Gemini Python SDK.

Provides a clean async interface to Gemini for text generation.
All retry logic, error handling, and API key management are
centralised here.

TODO: Implement async generate() with exponential backoff retry.
TODO: Implement generate_json() that enforces structured JSON output.
TODO: Add token usage logging.
TODO: Add API call rate limiting.
"""

from __future__ import annotations

from app.config.settings import get_settings


class GeminiClient:
    """Async client for Google Gemini AI text generation."""

    def __init__(self) -> None:
        settings = get_settings()
        self._api_key = settings.gemini_api_key
        self._model_name = settings.gemini_model
        # TODO: Initialise google.generativeai with api_key.
        # import google.generativeai as genai
        # genai.configure(api_key=self._api_key)
        # self._model = genai.GenerativeModel(self._model_name)

    async def generate(self, prompt: str) -> str:
        """
        Send a text prompt to Gemini and return the response text.

        Args:
            prompt: The full prompt string.

        Returns:
            Generated text response.

        TODO: Call self._model.generate_content_async(prompt).
        TODO: Extract and return response.text.
        TODO: Handle API errors and retry on 429 / 503.
        """
        raise NotImplementedError("GeminiClient.generate not implemented.")

    async def generate_json(self, prompt: str) -> dict:
        """
        Send a prompt to Gemini and parse the response as JSON.

        TODO: Append JSON format instruction to prompt.
        TODO: Call generate() and parse response.
        TODO: Validate that response is valid JSON.
        TODO: Retry on invalid JSON response.
        """
        raise NotImplementedError("GeminiClient.generate_json not implemented.")
