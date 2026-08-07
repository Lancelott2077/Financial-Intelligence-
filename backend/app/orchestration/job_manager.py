"""
orchestration/job_manager.py — Background job status tracking.

Manages background analysis job lifecycle — creation, progress updates,
and completion/failure notification.

TODO: Implement background task scheduling (FastAPI BackgroundTasks or Celery).
TODO: Implement job status polling endpoint support.
TODO: Add job cancellation support.
"""

from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from typing import Dict


class JobStatus(str, Enum):
    """Background job lifecycle status."""

    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Job:
    """
    Represents a background analysis job.

    Attributes:
        job_id      Unique job identifier (matches session_id).
        status      Current job status.
        progress    Completion percentage 0–100.
        error       Error message if status is FAILED.
    """

    job_id: str
    status: JobStatus = JobStatus.QUEUED
    progress: int = 0
    error: str | None = None


class JobManager:
    """Manages background analysis job lifecycle."""

    # In-memory store for development. Replace with Redis in production.
    _jobs: Dict[str, Job] = {}

    def create(self, job_id: str) -> Job:
        """
        Register a new background job.

        TODO: Create Job record and store in _jobs.
        TODO: Replace in-memory store with persistent backend.
        """
        raise NotImplementedError("JobManager.create not implemented.")

    def update_progress(self, job_id: str, progress: int) -> None:
        """
        Update job progress percentage.

        TODO: Look up job and update progress field.
        """
        raise NotImplementedError("JobManager.update_progress not implemented.")

    def complete(self, job_id: str) -> None:
        """Mark a job as completed."""
        raise NotImplementedError("JobManager.complete not implemented.")

    def fail(self, job_id: str, error: str) -> None:
        """Mark a job as failed with an error message."""
        raise NotImplementedError("JobManager.fail not implemented.")

    def get(self, job_id: str) -> Job | None:
        """Return the Job record for a given job_id."""
        raise NotImplementedError("JobManager.get not implemented.")
