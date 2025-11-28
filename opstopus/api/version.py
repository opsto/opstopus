"""
Version and endpoint information endpoint for Opstopus.
Route: /version
"""
import json
import falcon

# Application version
VERSION = "0.25.11"

# Endpoint registry for /version response
# NOTE: Update this list when adding new endpoints
ENDPOINTS = [
    {
        "path": "/health",
        "method": "GET",
        "description": "Health check endpoint for docker auto-heal or down monitoring"
    },
    {
        "path": "/version",
        "method": "GET",
        "description": "Returns current Opstopus version and list of available endpoints"
    }
]


class VersionResource:
    """Version and endpoint information resource."""

    def on_get(self, req, resp):
        """
        GET /version
        Returns current Opstopus version and exposed endpoints.
        
        Response:
            {
                "version": "x.x.x",
                "service": "opstopus",
                "endpoints": [...]
            }
        """
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = json.dumps({
            "version": VERSION,
            "service": "opstopus",
            "endpoints": ENDPOINTS
        })

