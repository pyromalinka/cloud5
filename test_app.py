import pytest
from app import app, cache

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200 
    assert b'Welcome!' in response.data 
    
# Тест маршрута /data с кэшированием
def test_data_page(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert b'This is some data!' in response.data

# Тест кэширования
def test_cache(client):
    response1 = client.get('/data')
    response2 = client.get('/data')
    assert response1.data == response2.data  # Данные должны быть одинаковыми, так как они кэшируются

# Тест ошибки 404
def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
