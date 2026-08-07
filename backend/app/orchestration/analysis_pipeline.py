"""
orchestration/analysis_pipeline.py — Full end-to-end analysis pipeline.

Sequences all analysis stages after a successful CSV upload:
  1. Data Processing   (CSVParser → Normaliser → Categoriser)
  2. Feature Extraction (FeatureMatrix)
  3. Behaviour Detection (DetectorRegistry)
  4. Evidence Persistence (EvidenceCollector)
  5. Decision Engine   (RuleEngine → DecisionBuilder)
  6. Plan Generation   (PlanService)

TODO: Implement full pipeline execution.
TODO: Emit progress events for real-time status updates.
TODO: Handle stage failures with partial recovery.
"""

from __future__ import annotations

from pathlib import Path
from sqlalchemy.orm import Session


class AnalysisPipeline:
    """Orchestrates the full analysis pipeline for an upload session."""

    def __init__(self, db: Session) -> None:
        self._db = db

    async def run(self, session_id: str, file_path: Path) -> None:
        """
        Execute the complete analysis pipeline for an upload session.

        Args:
            session_id: UUID of the UploadSession.
            file_path:  Path to the raw CSV file on disk.

        Pipeline stages:
            TODO Stage 1: ProcessingPipeline.run(session_id, file_path)
            TODO Stage 2: FeatureMatrix.build(transactions_df)
            TODO Stage 3: DetectorRegistry.run_all(feature_df)
            TODO Stage 4: EvidenceCollector.persist(session_id, results)
            TODO Stage 5: RuleEngine.evaluate(results, snapshot)
            TODO Stage 6: DecisionBuilder.build_plan(session_id, recommendations)
            TODO Stage 7: Update session status to 'completed'.
        """
        raise NotImplementedError("AnalysisPipeline.run not implemented.")
