import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.data == b'Hello from the Home Page...'

def test_about(client):
    response = client.get('/about')
    assert response.data == b'Hello from the About Page...'
