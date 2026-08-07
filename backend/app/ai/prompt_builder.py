"""
ai/prompt_builder.py — Constructs structured Gemini prompts from templates.

Loads prompt templates from the prompts/ directory and injects
session-specific financial context data.

TODO: Implement template loading from prompts/ directory.
TODO: Implement context injection for each prompt type.
"""

from __future__ import annotations

from pathlib import Path


PROMPTS_DIR = Path(__file__).resolve().parents[4] / "prompts"


class PromptBuilder:
    """Builds Gemini prompt strings from templates and session data."""

    def build_coach_prompt(
        self,
        user_message: str,
        snapshot: dict,
        behaviours: list[dict],
        history: list[dict],
    ) -> str:
        """
        Build the AI coach conversation prompt.

        TODO: Load system prompt template from prompts/coach_system.md.
        TODO: Inject snapshot and behaviour context.
        TODO: Append conversation history.
        TODO: Append current user message.
        """
        raise NotImplementedError("PromptBuilder.build_coach_prompt not implemented.")

    def build_categorisation_prompt(self, descriptions: list[str]) -> str:
        """
        Build a batch transaction categorisation prompt.

        TODO: Load template from prompts/categorisation.md.
        TODO: Inject transaction description list.
        TODO: Request JSON array response.
        """
        raise NotImplementedError(
            "PromptBuilder.build_categorisation_prompt not implemented."
        )
