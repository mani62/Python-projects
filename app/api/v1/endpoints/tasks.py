from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.services.task_service import TaskService
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()
service = TaskService()

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return service.get_tasks(db)

@router.get("/{task_uuid}", response_model=TaskResponse)
def get_task(task_uuid: UUID, db: Session = Depends(get_db)):
    task = service.get_task(db, task_uuid)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return service.create_task(db, task)

@router.put("/{task_uuid}", response_model=TaskResponse)
def update_task(task_uuid: UUID, data: TaskUpdate, db: Session = Depends(get_db)):
    task = service.update_task(db, task_uuid, data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_uuid}")
def delete_task(task_uuid: UUID, db: Session = Depends(get_db)):
    result = service.delete_task(db, task_uuid)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}