from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from typing import List
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import (
    get_tasks,
    get_task,
    create_task,
    update_task,
    delete_task,
)
from app.deps import get_db

# from app.auth import get_current_user
from app.schemas.user import User

router = APIRouter(prefix="/internal/tasks")
auth_scheme = HTTPBearer()


@router.get("/", response_model=List[Task])
def read_tasks(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    user = request.state.user
    tasks = get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.post("/", response_model=Task)
def create_new_task(
    request: Request,
    task: TaskCreate,
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    user = request.state.user
    return create_task(db, task, user_id=user.id)


@router.get("/{task_id}", response_model=Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/{task_id}", response_model=Task)
def update_existing_task(
    request: Request,
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.delete("/{task_id}", response_model=Task)
def delete_existing_task(
    request: Request,
    task_id: int,
    db: Session = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    db_task = delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
