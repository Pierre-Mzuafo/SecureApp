from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"

def test_create_and_get_item():
    response = client.post("/items", json={"name": "Test Item"})
    assert response.status_code == 201
    item = response.json()
    item_id = item["id"]

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Item"

def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_delete_item():
    response = client.post("/items", json={"name": "To Delete"})
    item_id = response.json()["id"]

    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
