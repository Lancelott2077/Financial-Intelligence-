"""
tests/test_behaviours.py — Behaviour detector unit tests.

TODO: Implement tests for each bias detector.
"""

import pytest


class TestPresentBiasDetector:
    """Tests for the Present Bias detector."""

    def test_detects_high_payday_spend(self):
        """TODO: Test detection when payday spend is high."""
        pytest.skip("PresentBiasDetector not yet implemented.")

    def test_no_detection_on_low_spend(self):
        """TODO: Test no detection on disciplined spending."""
        pytest.skip("PresentBiasDetector not yet implemented.")


class TestLossAversionDetector:
    """Tests for the Loss Aversion detector."""

    def test_detects_subscription_accumulation(self):
        """TODO: Test detection of excess subscription spending."""
        pytest.skip("LossAversionDetector not yet implemented.")


class TestDetectorRegistry:
    """Tests for the Detector Registry."""

    def test_run_all_returns_results(self):
        """TODO: Test that run_all returns a result per detector."""
        pytest.skip("DetectorRegistry not yet implemented.")
