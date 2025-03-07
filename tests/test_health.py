"""
Tests for the health endpoint
"""
from fastapi.testclient import TestClient

from src.mcp_server.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test that the health endpoint returns a 200 status code."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root_endpoint():
    """Test that the root endpoint returns basic information."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "description" in data 