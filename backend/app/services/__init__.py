"""
services package — Business logic layer.

Services sit between API route handlers and the lower-level
processing / AI layers. They contain all orchestration logic
and database access patterns.

Modules:
    upload_service      Handles file persistence and session creation.
    snapshot_service    Aggregates transaction data into a snapshot.
    behaviour_service   Retrieves and formats detected behaviours.
    savings_service     Generates ranked savings opportunities.
    coach_service       Manages AI coaching conversation state.
    plan_service        Builds and manages personalised action plans.
"""
