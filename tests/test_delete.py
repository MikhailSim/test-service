import requests

base_url = "http://localhost:8080"

def test_delete_entity():
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

    # Удаление сущности
    delete_response = requests.delete(f"{base_url}/api/delete/{entity_id}")
    assert delete_response.status_code == 204
