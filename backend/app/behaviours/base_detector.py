"""
behaviours/base_detector.py — Abstract base class for all bias detectors.

Every detector must inherit from BaseBiasDetector and implement detect().
This enforces a consistent interface across all detector modules.

TODO: Define the full DetectionResult dataclass.
TODO: Define threshold configuration (per-detector settings).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

import pandas as pd

from app.schemas.common import BiasType, SeverityLevel


@dataclass
class DetectionResult:
    """
    Result returned by a single bias detector.

    Attributes:
        bias_type       Unique identifier string for the bias type.
        detected        Whether the bias was detected.
        confidence      Confidence score 0.0–1.0.
        severity        'low' | 'medium' | 'high'.
        summary         Human-readable summary of the detection.
        evidence_ids    Transaction IDs that constitute evidence.
    """

    bias_type: BiasType
    detected: bool
    confidence: float = 0.0
    severity: SeverityLevel = SeverityLevel.LOW
    summary: str = ""
    evidence_ids: List[int] = field(default_factory=list)


class BaseBiasDetector(ABC):
    """
    Abstract base class that all bias detectors must implement.

    Each subclass targets a specific cognitive bias and analyses the
    feature-enriched transaction DataFrame.
    """

    # Subclasses must override these.
    BIAS_TYPE: str = ""
    DISPLAY_NAME: str = ""

    @abstractmethod
    def detect(self, df: pd.DataFrame) -> DetectionResult:
        """
        Analyse the feature DataFrame and return a DetectionResult.

        Args:
            df: Feature-enriched transaction DataFrame from FeatureMatrix.

        Returns:
            DetectionResult for this detector's bias type.
        """
        ...
