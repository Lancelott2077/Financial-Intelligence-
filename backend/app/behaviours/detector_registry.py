"""
behaviours/detector_registry.py — Central registry of all bias detectors.

The registry holds all active detector instances and exposes a single
run_all() method that executes every detector and collects results.

TODO: Register all detector classes below.
TODO: Add enable/disable mechanism per detector.
TODO: Support parallel detector execution.
"""

from __future__ import annotations

from typing import List
import pandas as pd

from app.behaviours.base_detector import BaseBiasDetector, DetectionResult
from app.behaviours.present_bias import PresentBiasDetector
from app.behaviours.loss_aversion import LossAversionDetector
from app.behaviours.anchoring import AnchoringDetector
from app.behaviours.mental_accounting import MentalAccountingDetector
from app.behaviours.status_quo_bias import StatusQuoBiasDetector


class DetectorRegistry:
    """Registry that runs all registered bias detectors."""

    # TODO: Add more detectors as they are implemented.
    _DETECTORS: List[type[BaseBiasDetector]] = [
        PresentBiasDetector,
        LossAversionDetector,
        AnchoringDetector,
        MentalAccountingDetector,
        StatusQuoBiasDetector,
    ]

    def __init__(self) -> None:
        self._instances: List[BaseBiasDetector] = [
            cls() for cls in self._DETECTORS
        ]

    def run_all(self, df: pd.DataFrame) -> List[DetectionResult]:
        """
        Execute all registered detectors against the feature DataFrame.

        Args:
            df: Feature-enriched transaction DataFrame.

        Returns:
            List of DetectionResult — one per detector.

        TODO: Execute detectors.
        TODO: Filter to only return detected=True results.
        TODO: Sort by confidence descending.
        """
        raise NotImplementedError("DetectorRegistry.run_all not implemented.")
