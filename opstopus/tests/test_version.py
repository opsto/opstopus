"""
Tests for the /version endpoint.
"""
import falcon

from api.version import VERSION, ENDPOINTS


class TestVersionEndpoint:
    """Test cases for the version endpoint."""

    def test_version_returns_200(self, client):
        """Test that /version returns HTTP 200 OK."""
        result = client.simulate_get("/version")
        assert result.status == falcon.HTTP_200

    def test_version_returns_json(self, client):
        """Test that /version returns JSON content type."""
        result = client.simulate_get("/version")
        assert result.headers.get("content-type") == "application/json"

    def test_version_response_structure(self, client):
        """Test that /version returns expected JSON structure."""
        result = client.simulate_get("/version")
        data = result.json
        
        assert "version" in data
        assert "service" in data
        assert "endpoints" in data

    def test_version_contains_correct_version(self, client):
        """Test that /version returns the correct version string."""
        result = client.simulate_get("/version")
        data = result.json
        
        assert data["version"] == VERSION
        assert data["service"] == "opstopus"

    def test_version_endpoints_list(self, client):
        """Test that /version returns the endpoints list."""
        result = client.simulate_get("/version")
        data = result.json
        
        assert isinstance(data["endpoints"], list)
        assert len(data["endpoints"]) == len(ENDPOINTS)

    def test_version_endpoints_structure(self, client):
        """Test that each endpoint in the list has the required fields."""
        result = client.simulate_get("/version")
        data = result.json
        
        for endpoint in data["endpoints"]:
            assert "path" in endpoint
            assert "method" in endpoint
            assert "description" in endpoint

    def test_version_includes_health_endpoint(self, client):
        """Test that /health is listed in the endpoints."""
        result = client.simulate_get("/version")
        data = result.json
        
        paths = [ep["path"] for ep in data["endpoints"]]
        assert "/health" in paths

    def test_version_includes_version_endpoint(self, client):
        """Test that /version is listed in the endpoints."""
        result = client.simulate_get("/version")
        data = result.json
        
        paths = [ep["path"] for ep in data["endpoints"]]
        assert "/version" in paths

