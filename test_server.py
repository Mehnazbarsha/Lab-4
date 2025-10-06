import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("my_server", "my-server.py")
my_server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_server)
app = my_server.app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_factor_12(client):
    """Test factoring 12 - should return [1, 2, 2, 3]"""
    response = client.get('/factor?number=12')
    assert response.status_code == 200
    assert response.get_json() == [1, 2, 2, 3]

def test_factor_prime_13(client):
    """Test factoring prime 13 - should return [1, 13]"""
    response = client.get('/factor?number=13')
    assert response.status_code == 200
    assert response.get_json() == [1, 13]

def test_factor_error(client):
    """Test missing parameter - should return 400 error"""
    response = client.get('/factor')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data