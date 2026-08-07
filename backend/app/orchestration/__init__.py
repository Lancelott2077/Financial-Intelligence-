"""
orchestration package — Pipeline orchestration and job management.

Coordinates the end-to-end analysis pipeline triggered after
a CSV upload, sequencing all stages from ingestion to plan generation.

Modules:
    analysis_pipeline   Full analysis pipeline from raw CSV to action plan.
    job_manager         Background job management (status tracking).
"""
