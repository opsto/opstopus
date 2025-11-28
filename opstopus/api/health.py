"""
Health check endpoint for Opstopus.
Route: /health
"""
import json
import falcon


class HealthResource:
    """Health check endpoint for container monitoring."""

    def on_get(self, req, resp):
        """
        GET /health
        Returns health status for docker auto-heal or monitoring systems.
        
        Response:
            {
                "status": "healthy",
                "service": "opstopus"
            }
        """
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = json.dumps({
            "status": "healthy",
            "service": "opstopus"
        })

