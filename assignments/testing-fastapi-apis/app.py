from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


tasks: dict[int, Task] = {
    1: Task(id=1, title="Read a book", completed=False),
}
next_task_id = 2


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = Task(id=next_task_id, **task_data.model_dump())
    tasks[next_task_id] = task
    next_task_id += 1
    return task