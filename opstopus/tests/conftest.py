"""
Pytest fixtures for Opstopus API tests.
"""
import pytest
from falcon import testing

from app import create_app


@pytest.fixture()
def client():
    """
    Create a test client for the Opstopus application.
    
    This fixture provides a falcon.testing.TestClient instance
    that can be used to simulate HTTP requests to the application.
    """
    return testing.TestClient(create_app())

