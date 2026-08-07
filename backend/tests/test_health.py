"""
tests/test_health.py — Health check endpoint tests.

Tests that the API server starts and the health endpoint responds correctly.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """GET /health should return 200 with status 'ok'."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data


# TODO: Add more integration tests as endpoints are implemented.
