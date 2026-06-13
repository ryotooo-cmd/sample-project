import pytest

from app import app, todos


@pytest.fixture
def client():
    todos.clear()
    with app.test_client() as client:
        yield client


def test_list_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_todo(client):
    response = client.post("/todos", json={"title": "Buy milk"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Buy milk"
    assert data["done"] is False
    assert "id" in data


def test_create_todo_without_title(client):
    response = client.post("/todos", json={})
    assert response.status_code == 400


def test_get_todo(client):
    created = client.post("/todos", json={"title": "Read book"}).get_json()
    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Read book"


def test_get_todo_not_found(client):
    response = client.get("/todos/999")
    assert response.status_code == 404


def test_update_todo(client):
    created = client.post("/todos", json={"title": "Write code"}).get_json()
    response = client.patch(f"/todos/{created['id']}", json={"done": True})
    assert response.status_code == 200
    assert response.get_json()["done"] is True


def test_delete_todo(client):
    created = client.post("/todos", json={"title": "Cleanup"}).get_json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.status_code == 204
    assert client.get(f"/todos/{created['id']}").status_code == 404
