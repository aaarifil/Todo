from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from services.todo_service import ToDoService
from repositories.db_todo_repository import DBToDoRepository
from schemas.todo import (
    ToDoCreate,
    ToDoResponse,
    ToDoListResponse,
    ToDoUpdate,
)
from core.db import get_session
from sqlmodel import Session

router = APIRouter()


def get_repo(session: Session = Depends(get_session)) -> DBToDoRepository:
    return DBToDoRepository(session)


@router.post("/todos", response_model=ToDoResponse)
def create_todo(payload: ToDoCreate, repo: DBToDoRepository = Depends(get_repo)):
    service = ToDoService(repo)
    item = service.create(payload)
    return item


@router.get("/todos", response_model=ToDoListResponse)
def list_todos(
    is_done: Optional[bool] = Query(None),
    q: Optional[str] = Query(None),
    sort: str = Query("created_at"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    repo: DBToDoRepository = Depends(get_repo),
):
    service = ToDoService(repo)
    items, total = service.list(is_done=is_done, q=q, sort=sort, limit=limit, offset=offset)
    return {"items": items, "total": total, "limit": limit, "offset": offset}


@router.get("/todos/{id}", response_model=ToDoResponse)
def get_todo(id: int, repo: DBToDoRepository = Depends(get_repo)):
    service = ToDoService(repo)
    item = service.get(id)
    if not item:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return item


@router.put("/todos/{id}", response_model=ToDoResponse)
def put_todo(id: int, payload: ToDoCreate, repo: DBToDoRepository = Depends(get_repo)):
    # replace semantics: update all fields
    from schemas.todo import ToDoUpdate

    update = ToDoUpdate(title=payload.title, description=payload.description, is_done=payload.is_done)
    service = ToDoService(repo)
    item = service.update(id, update)
    if not item:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return item


@router.delete("/todos/{id}")
def delete_todo(id: int, repo: DBToDoRepository = Depends(get_repo)):
    service = ToDoService(repo)
    ok = service.delete(id)
    if not ok:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return {"ok": True}


@router.patch("/todos/{id}", response_model=ToDoResponse)
def patch_todo(id: int, payload: ToDoUpdate, repo: DBToDoRepository = Depends(get_repo)):
    service = ToDoService(repo)
    item = service.update(id, payload)
    if not item:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return item
