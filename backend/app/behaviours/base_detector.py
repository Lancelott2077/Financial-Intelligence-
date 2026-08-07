"""
behaviours/base_detector.py — Abstract base class for all bias detectors.

Every detector must inherit from BaseBiasDetector and implement detect().
This enforces a consistent interface across all detector modules.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import pandas as pd

from app.schemas.common import BiasType, SeverityLevel


@dataclass
class DetectionResult:
    """
    Result returned by a single bias detector.

    Attributes:
        bias_type:       Unique identifier string for the bias type.
        detected:        Whether the bias was detected.
        confidence:      Confidence score 0.0–1.0.
        severity:        'low' | 'medium' | 'high'.
        summary:         Human-readable summary of the detection.
        evidence_ids:    Transaction IDs that constitute evidence.
    """

    bias_type: BiasType
    detected: bool
    confidence: float = 0.0
    severity: SeverityLevel = SeverityLevel.LOW
    summary: str = ""
    evidence_ids: List[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate detector outputs to ensure data integrity."""
        # Validate confidence score bounds
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"Confidence score must be between 0.0 and 1.0, got {self.confidence}")

        # Validate logic when bias is detected
        if self.detected:
            if not self.summary.strip():
                raise ValueError("A summary must be provided if a bias is detected.")
            if self.confidence == 0.0:
                raise ValueError("Confidence must be > 0.0 if a bias is detected.")
        else:
            if self.evidence_ids:
                raise ValueError("Evidence IDs should not be provided if a bias is not detected.")

        # Ensure enums are properly cast if passed as strings
        if not isinstance(self.bias_type, BiasType):
            try:
                self.bias_type = BiasType(self.bias_type)
            except ValueError as e:
                raise ValueError(f"Invalid bias_type: {self.bias_type}") from e

        if not isinstance(self.severity, SeverityLevel):
            try:
                self.severity = SeverityLevel(self.severity)
            except ValueError as e:
                raise ValueError(f"Invalid severity level: {self.severity}") from e


@dataclass
class DetectorConfig:
    """
    Configuration settings and thresholds for a behaviour detector.
    
    Attributes:
        confidence_threshold: Minimum confidence required to flag as detected.
        min_evidence_count: Minimum number of transactions to form evidence.
        parameters: Additional detector-specific configuration parameters.
    """
    confidence_threshold: float = 0.5
    min_evidence_count: int = 1
    parameters: Dict[str, Any] = field(default_factory=dict)


class BaseBiasDetector(ABC):
    """
    Abstract base class that all bias detectors must implement.

    Each subclass targets a specific cognitive bias and analyses the
    feature-enriched transaction DataFrame.
    """

    # Subclasses must override these class attributes.
    BIAS_TYPE: str = ""
    DISPLAY_NAME: str = ""

    def __init__(self, config: Optional[DetectorConfig] = None) -> None:
        """
        Initialise the detector with optional configuration.
        
        Args:
            config: Thresholds and settings for this detector.
        """
        self.config = config or DetectorConfig()
        self._validate_detector_configuration()

    def _validate_detector_configuration(self) -> None:
        """Ensure the subclass has correctly defined required attributes."""
        if not self.BIAS_TYPE:
            raise ValueError(f"{self.__class__.__name__} must define a BIAS_TYPE.")
        if not self.DISPLAY_NAME:
            raise ValueError(f"{self.__class__.__name__} must define a DISPLAY_NAME.")
            
        # Ensure BIAS_TYPE is a valid registered BiasType
        try:
            BiasType(self.BIAS_TYPE)
        except ValueError as e:
            raise ValueError(
                f"{self.__class__.__name__}.BIAS_TYPE '{self.BIAS_TYPE}' "
                f"is not a valid BiasType enum value."
            ) from e

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
