from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class Task(BaseModel):
    id: Optional[int] = None
    name: str
    completed: bool

tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Lista de Tarefas construída com FastAPI!"}

@app.get("/tasks", response_model=List[Task])
async def read_tasks(completed: Optional[bool] = None):
    if completed is None:
        return tasks
    return [task for task in tasks if task.completed == completed]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    for index, stored_task in enumerate(tasks):
        if stored_task.id == task_id:
            tasks[index] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index, stored_task in enumerate(tasks):
        if stored_task.id == task_id:
            tasks.pop(index)
            return {"message": "Task has been deleted successfully!"}
    raise HTTPException(status_code=404, detail="Task not found")