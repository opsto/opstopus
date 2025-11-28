"""
Opstopus Backend Application
Falcon-based REST API for Opstopus management.

Route Organization:
    Each endpoint is implemented as a separate Python file in the api/ folder.
    Example:
        /health  -> api/health.py  (HealthResource)
        /version -> api/version.py (VersionResource)

    To add a new endpoint:
        1. Create a new file in api/ folder (e.g., api/myendpoint.py)
        2. Implement the resource class with on_get/on_post/etc methods
        3. Import and register the route in this file's create_app() function
        4. Update api/version.py ENDPOINTS list with the new endpoint info
"""
import falcon

from api import HealthResource, VersionResource


def create_app():
    """Create and configure the Falcon application."""
    app = falcon.App()

    # Register routes
    # Each route corresponds to a resource in the api/ folder
    app.add_route("/health", HealthResource())    # api/health.py
    app.add_route("/version", VersionResource())  # api/version.py

    return app


# WSGI application instance for gunicorn
application = create_app()

