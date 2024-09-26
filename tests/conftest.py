import pytest
import requests

BASE_URL = "http://localhost:8080"

@pytest.fixture(scope="module")
def create_entity():
    payload = {
        "name": "Test Entity",
        "value": "Test Value"
    }
    response = requests.post(f"{BASE_URL}/api/create", json=payload)
    return response.json()

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL
