from fastapi.testclient import TestClient
from main import app, Task

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à Lista de Tarefas construída com FastAPI!"}

def test_read_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_create_task():
    response = client.post(
        "/tasks",
        json={"name": "Test Task", "completed": False},
    )
    assert response.status_code == 200
    task = response.json()
    assert task["name"] == "Test Task"
    assert task["completed"] == False
    assert "id" in task

def test_read_tasks_with_data():
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) > 0
    for task in tasks:
        assert "name" in task
        assert "completed" in task
        assert "id" in task