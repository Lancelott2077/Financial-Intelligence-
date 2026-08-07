"""
processing/pipeline.py — Data processing pipeline orchestrator.

Chains CSVParser → Normaliser → Categoriser and persists
the resulting transactions to the database.

TODO: Implement full pipeline execution.
TODO: Update UploadSession status at each stage.
TODO: Handle and log pipeline failures gracefully.
"""

from __future__ import annotations

from pathlib import Path
from sqlalchemy.orm import Session

from app.processing.csv_parser import CSVParser
from app.processing.normaliser import Normaliser
from app.processing.categoriser import Categoriser


class ProcessingPipeline:
    """Orchestrates the CSV → normalised transactions pipeline."""

    def __init__(self, db: Session) -> None:
        self._db = db
        self._parser = CSVParser()
        self._normaliser = Normaliser()
        self._categoriser = Categoriser()

    async def run(self, session_id: str, file_path: Path) -> None:
        """
        Execute the full data processing pipeline for a session.

        Args:
            session_id: UUID of the UploadSession.
            file_path:  Path to the raw CSV file on disk.

        TODO: Update session status to 'processing'.
        TODO: Parse CSV → raw DataFrame.
        TODO: Detect columns → column_map.
        TODO: Normalise → normalised DataFrame.
        TODO: Categorise → categorised DataFrame.
        TODO: Persist transactions to DB.
        TODO: Update session status to 'completed' or 'failed'.
        """
        raise NotImplementedError("ProcessingPipeline.run not implemented.")
