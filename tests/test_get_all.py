import requests

base_url = "http://localhost:8080"

def test_get_all_entities():
    # Получение всех сущностей
    get_all_response = requests.get(f"{base_url}/api/getAll")
    assert get_all_response.status_code == 200
    entities = get_all_response.json()['entity']  # сервер возвращает объект с ключом 'entity'
    assert isinstance(entities, list)
