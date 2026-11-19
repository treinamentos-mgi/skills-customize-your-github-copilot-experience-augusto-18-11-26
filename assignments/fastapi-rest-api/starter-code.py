from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/", tags=["status"])
def read_root():
    return {"message": "Task API is running"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())