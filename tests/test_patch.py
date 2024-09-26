import requests

base_url = "http://localhost:8080"


def test_patch_entity():
    try:
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
        create_response.raise_for_status()  # Проверка успешности запроса
        assert create_response.status_code == 200
        entity_id = create_response.json()

        # Обновление сущности
        patch_payload = {"title": "Обновлённый заголовок"}
        patch_response = requests.patch(f"{base_url}/api/patch/{entity_id}", json=patch_payload)
        patch_response.raise_for_status()
        assert patch_response.status_code in [200, 204]  # Обновление может вернуть 204 или 200

        # Проверка обновления
        get_response = requests.get(f"{base_url}/api/get/{entity_id}")
        get_response.raise_for_status()
        assert get_response.status_code == 200
        entity = get_response.json()
        assert entity['title'] == "Обновлённый заголовок"
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        assert False, "Test failed due to request error"
