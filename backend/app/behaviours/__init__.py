"""
behaviours package — Cognitive bias / behavioural bias detectors.

Each module implements a detector for a specific class of financial behaviour.
All detectors share the BaseBiasDetector interface.

Modules:
    base_detector           Abstract base class for all detectors.
    present_bias            Detects present bias (short-term preference over long-term).
    loss_aversion           Detects loss aversion (holding losing positions).
    anchoring               Detects anchoring to reference prices.
    mental_accounting       Detects mental accounting (siloed spending buckets).
    herd_behaviour          Detects herd / social spending behaviour.
    status_quo_bias         Detects status quo / inertia behaviour.
    detector_registry       Registry of all active detectors.
"""
