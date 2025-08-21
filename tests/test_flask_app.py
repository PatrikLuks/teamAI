import json
from src.app import app


def test_add_todo():
    client = app.test_client()
    response = client.post("/todos", json={"task": "Test Task"})
    assert response.status_code == 201


def test_get_todos():
    client = app.test_client()
    client.post("/todos", json={"task": "Another Task"})
    response = client.get("/todos")
    data = json.loads(response.data)
    assert "Another Task" in data
