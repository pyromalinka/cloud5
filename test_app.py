import pytest
from app import app, cache

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'message' in json_data
    assert json_data['message'].startswith('Welcome from')
    
def test_data_page(client):
    response = client.get('/data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {'data': 'This is some data!'}

def test_cache(client):
    response1 = client.get('/data')
    response2 = client.get('/data')
    assert response1.get_json() == response2.get_json()

def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
