"""
behaviours/detector_registry.py — Central registry of all bias detectors.

The registry holds all active detector instances and exposes a single
run_all() method that executes every detector and collects results.

TODO: Add enable/disable mechanism per detector.
TODO: Support parallel detector execution.
"""

from __future__ import annotations

from typing import List
import pandas as pd
from loguru import logger

from app.behaviours.base_detector import BaseBiasDetector, DetectionResult
from app.behaviours.present_bias import PresentBiasDetector
from app.behaviours.loss_aversion import LossAversionDetector
from app.behaviours.anchoring import AnchoringDetector
from app.behaviours.mental_accounting import MentalAccountingDetector
from app.behaviours.status_quo_bias import StatusQuoBiasDetector


class DetectorRegistry:
    """Registry that runs all registered bias detectors."""

    _DETECTORS: List[type[BaseBiasDetector]] = [
        PresentBiasDetector,
        LossAversionDetector,
        AnchoringDetector,
        MentalAccountingDetector,
        StatusQuoBiasDetector,
    ]

    def __init__(self) -> None:
        """Initialize the registry and instantiate all active detectors."""
        self._instances: List[BaseBiasDetector] = []
        for cls in self._DETECTORS:
            try:
                self._instances.append(cls())
            except Exception as e:
                logger.error(f"Failed to instantiate detector {cls.__name__}: {e}")

    def run_all(self, df: pd.DataFrame) -> List[DetectionResult]:
        """
        Execute all registered detectors against the feature DataFrame.

        Args:
            df: Feature-enriched transaction DataFrame.

        Returns:
            List of DetectionResult for all detectors in execution order.
        """
        results: List[DetectionResult] = []

        for detector in self._instances:
            try:
                result = detector.detect(df)
                results.append(result)
            except Exception as e:
                logger.error(
                    f"Detector {detector.__class__.__name__} failed during execution: {e}",
                    exc_info=True
                )

        return results
