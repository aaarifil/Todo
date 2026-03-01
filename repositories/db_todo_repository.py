from typing import Optional, Tuple, List
from sqlmodel import Session, select
from sqlalchemy import func
from models.models import ToDo
from schemas.todo import ToDoCreate, ToDoUpdate
from datetime import datetime


class DBToDoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, obj_in: ToDoCreate, owner_id: Optional[int] = None) -> ToDo:
        todo = ToDo(
            title=obj_in.title,
            description=obj_in.description,
            is_done=obj_in.is_done,
            owner_id=owner_id,
        )
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def list(
        self,
        is_done: Optional[bool] = None,
        q: Optional[str] = None,
        sort: str = "created_at",
        limit: int = 10,
        offset: int = 0,
    ) -> Tuple[List[ToDo], int]:
        stmt = select(ToDo)
        if is_done is not None:
            stmt = stmt.where(ToDo.is_done == is_done)
        if q:
            stmt = stmt.where(ToDo.title.ilike(f"%{q}%"))

        reverse = False
        key = "created_at"
        if sort.startswith("-"):
            reverse = True
            key = sort[1:]
        else:
            key = sort

        if hasattr(ToDo, key):
            col = getattr(ToDo, key)
            if reverse:
                stmt = stmt.order_by(col.desc())
            else:
                stmt = stmt.order_by(col)

        total = self.session.exec(select([ToDo]).where(stmt._whereclause) if stmt._whereclause is not None else select(ToDo)).all() if False else None
        # simpler total query
        # build count query with same filters
        count_stmt = select(func.count()).select_from(ToDo)
        if is_done is not None:
            count_stmt = count_stmt.where(ToDo.is_done == is_done)
        if q:
            count_stmt = count_stmt.where(ToDo.title.ilike(f"%{q}%"))

        res = self.session.exec(count_stmt).first()
        if res is None:
            total = 0
        elif isinstance(res, tuple):
            total = int(res[0])
        else:
            total = int(res)

        results = self.session.exec(stmt.offset(offset).limit(limit)).all()
        return results, int(total)

    def get(self, id: int) -> Optional[ToDo]:
        return self.session.get(ToDo, id)

    def update(self, id: int, obj_in: ToDoUpdate) -> Optional[ToDo]:
        todo = self.get(id)
        if not todo:
            return None
        if obj_in.title is not None:
            todo.title = obj_in.title
        if obj_in.description is not None:
            todo.description = obj_in.description
        if obj_in.is_done is not None:
            todo.is_done = obj_in.is_done
        todo.updated_at = datetime.utcnow()
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def delete(self, id: int) -> bool:
        todo = self.get(id)
        if not todo:
            return False
        self.session.delete(todo)
        self.session.commit()
        return True
