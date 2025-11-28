"""
Tests for the /health endpoint.
"""
import falcon


class TestHealthEndpoint:
    """Test cases for the health check endpoint."""

    def test_health_returns_200(self, client):
        """Test that /health returns HTTP 200 OK."""
        result = client.simulate_get("/health")
        assert result.status == falcon.HTTP_200

    def test_health_returns_json(self, client):
        """Test that /health returns JSON content type."""
        result = client.simulate_get("/health")
        assert result.headers.get("content-type") == "application/json"

    def test_health_response_structure(self, client):
        """Test that /health returns expected JSON structure."""
        result = client.simulate_get("/health")
        data = result.json
        
        assert "status" in data
        assert "service" in data

    def test_health_status_healthy(self, client):
        """Test that /health reports healthy status."""
        result = client.simulate_get("/health")
        data = result.json
        
        assert data["status"] == "healthy"
        assert data["service"] == "opstopus"

