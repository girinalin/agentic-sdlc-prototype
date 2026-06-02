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

async def test_update_item_success():
    item_data = {"name": "Updated Item"}
    response = await client.put("/items/123", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["item"]["name"] == "Updated Item"

async def test_update_item_not_found():
    response = await client.put("/items/999", json={"name": "Nonexistent"})
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Item not found"
