"""
Opstopus API Routes Module.

Each endpoint is implemented as a separate Python file in this folder.
Example:
    /health  -> api/health.py
    /version -> api/version.py
"""
from api.health import HealthResource
from api.version import VersionResource

__all__ = ["HealthResource", "VersionResource"]

