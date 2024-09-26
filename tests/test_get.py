import requests

base_url = "http://localhost:8080"


def test_get_entity():
    # Создание сущности
    payload = {
        "addition": {
            "additional_info": "Дополнительные сведения",
            "additional_number": 123
        },
        "important_numbers": [42, 87, 15],
        "title": "Заголовок сущности",
        "verified": True
    }
    create_response = requests.post(f"{base_url}/api/create", json=payload)
    assert create_response.status_code == 200
    entity_id = create_response.json()  # сервер возвращает id, а не объект

    # Получение сущности
    get_response = requests.get(f"{base_url}/api/get/{entity_id}")
    assert get_response.status_code == 200
    entity = get_response.json()
    assert entity['title'] == "Заголовок сущности"
