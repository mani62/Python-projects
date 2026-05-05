from datetime import datetime, timezone
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate
from fastapi import HTTPException
class TaskService:

    def get_tasks(self, db: Session):
        return db.query(Task).all()
    
    def get_task(self, db: Session, task_uuid: UUID):
        return db.query(Task).filter(Task.uuid==task_uuid).first()

    def create_task(self, db: Session, task: TaskCreate):
        task = Task(
            title=task.title,
            description=task.description
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    
    def update_task(self, db: Session, task_uuid: UUID, task_data: TaskUpdate):
        task = self.get_task(db, task_uuid)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        update_data = task_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)

        return task

    def delete_task(self, db: Session, task_uuid: UUID):
        task = self.get_task(db, task_uuid)
        if not task:
            return None
        
        task.deleted_at=datetime.now(timezone.utc)
        db.commit()
        return True    