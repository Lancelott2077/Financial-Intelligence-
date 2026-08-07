"""
evidence package — Evidence collection and persistence layer.

Bridges the behaviour detection layer and the database.
Responsible for persisting DetectionResults and their supporting
transaction evidence records.

Modules:
    evidence_collector      Persists DetectionResult to DB.
    evidence_formatter      Formats DB records into API schema models.
"""
