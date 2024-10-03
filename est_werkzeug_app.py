import pytest
from werkzeug.wrappers import Response
from werkzeug_app import application  # Adjust this import based on your file structure

@pytest.fixture
def client():
    """A test client for the application."""
    from werkzeug.test import Client
    return Client(application, Response)

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Home Page!' in response.data

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About This Application' in response.data

def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404 Not Found' in response.data
