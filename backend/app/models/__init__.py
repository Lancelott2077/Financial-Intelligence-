"""
models package — SQLAlchemy ORM models.

Each module defines the database table(s) for one domain entity.

Modules:
    session         UploadSession — tracks a CSV upload lifecycle.
    transaction     Transaction — normalised bank transaction row.
    behaviour       DetectedBehaviour — a detected cognitive bias.
    evidence        BehaviourEvidence — evidence supporting a bias.
    plan            ActionPlanItem — a single actionable recommendation.
"""
