"""
ai package — Google Gemini AI integration.

All Gemini API interactions are isolated in this package.
The rest of the application interacts with AI only through
the GeminiClient interface.

Modules:
    gemini_client       Thin wrapper around the Gemini Python SDK.
    prompt_builder      Constructs structured prompts from templates.
    response_parser     Parses and validates Gemini JSON responses.
"""
