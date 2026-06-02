from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_and_get_item():
    response = client.post("/api/items", json={"name": "Item1"})
    assert response.status_code == 201
    item_id = response.json()["id"]

    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Item1"
