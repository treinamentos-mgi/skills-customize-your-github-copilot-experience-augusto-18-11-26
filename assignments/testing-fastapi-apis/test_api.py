import pytest
from fastapi.testclient import TestClient

import app as task_api


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(
        task_api,
        "tasks",
        {1: task_api.Task(id=1, title="Read a book", completed=False)},
    )
    monkeypatch.setattr(task_api, "next_task_id", 2)
    return TestClient(task_api.app)


def test_list_tasks_returns_saved_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Read a book", "completed": False},
    ]


def test_get_existing_task_returns_task(client):
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Read a book",
        "completed": False,
    }