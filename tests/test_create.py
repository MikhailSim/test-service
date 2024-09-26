import requests

base_url = "http://localhost:8080"


def test_create_entity():
    payload = {
        "addition": {
            "additional_info": "Дополнительные сведения",
            "additional_number": 123
        },
        "important_numbers": [
            42,
            87,
            15
        ],
        "title": "Заголовок сущности",
        "verified": True
    }

    response = requests.post(f"{base_url}/api/create", json=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
