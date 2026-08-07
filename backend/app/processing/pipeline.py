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

import pandas as pd
import logging

logger = logging.getLogger(__name__)


class ProcessingPipeline:
    """Orchestrates the CSV → normalised transactions pipeline."""

    def __init__(self, db: Session) -> None:
        self._db = db
        self._parser = CSVParser()
        self._normaliser = Normaliser()
        self._categoriser = Categoriser()

    async def run(self, session_id: str, file_path: Path) -> pd.DataFrame:
        """
        Execute the full deterministic data processing pipeline for a session.

        Args:
            session_id: UUID of the UploadSession.
            file_path:  Path to the raw CSV file on disk.
            
        Returns:
            Fully processed pandas DataFrame.
        """
        logger.info("Starting processing pipeline for session %s", session_id)
        
        # 1. Parse CSV
        logger.debug("Parsing CSV file: %s", file_path)
        raw_df = self._parser.parse(file_path)
        
        # 2. Detect Columns
        logger.debug("Detecting standard columns")
        column_map = self._parser.detect_columns(raw_df)
        
        # 3. Normalise Data
        logger.debug("Normalising transaction data")
        norm_df = self._normaliser.normalise(raw_df, column_map)
        
        # 4. Categorise Data
        logger.debug("Categorising transactions")
        cat_df = self._categoriser.categorise(norm_df)
        
        logger.info("Pipeline completed successfully for session %s. Processed %d valid transactions.", session_id, len(cat_df))
        return cat_df
