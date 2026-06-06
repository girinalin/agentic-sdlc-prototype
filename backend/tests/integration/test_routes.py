import pytest
from fastapi.testclient import TestClient

from backend.src.api.dependencies import service
from backend.src.main import app


@pytest.fixture
def client():
    service.db.items.clear()
    with TestClient(app) as test_client:
        yield test_client


def test_create_and_get_item(client):
    response = client.post("/api/items", json={"name": "Item1"})
    assert response.status_code == 201
    item_id = response.json()["id"]

    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Item1"


def test_update_item_success(client):
    create_response = client.post("/api/items", json={"name": "Original"})
    item_id = create_response.json()["id"]

    response = client.put(
        f"/api/items/{item_id}",
        json={"name": "Updated Item", "description": "Updated description"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item"
    assert data["description"] == "Updated description"


def test_update_item_not_found(client):
    response = client.put("/api/items/999", json={"name": "Nonexistent"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_delete_item(client):
    create_response = client.post("/api/items", json={"name": "Delete me"})
    item_id = create_response.json()["id"]

    response = client.delete(f"/api/items/{item_id}")

    assert response.status_code == 204
    assert client.get(f"/api/items/{item_id}").status_code == 404


def test_delete_item_not_found(client):
    response = client.delete("/api/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
