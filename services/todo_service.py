from typing import Optional, Tuple, Any
from schemas.todo import ToDoCreate, ToDoUpdate, ToDoInDB


class ToDoService:
    def __init__(self, repo: Any):
        self.repo = repo

    def create(self, obj_in: ToDoCreate) -> ToDoInDB:
        return self.repo.create(obj_in)

    def list(
        self,
        is_done: Optional[bool] = None,
        q: Optional[str] = None,
        sort: str = "created_at",
        limit: int = 10,
        offset: int = 0,
    ) -> Tuple[list[ToDoInDB], int]:
        # repo may implement `list(...)` or legacy `filter_sort_paginate(...)`
        if hasattr(self.repo, "list"):
            return self.repo.list(is_done=is_done, q=q, sort=sort, limit=limit, offset=offset)
        return self.repo.filter_sort_paginate(is_done=is_done, q=q, sort=sort, limit=limit, offset=offset)

    def get(self, id: int) -> Optional[ToDoInDB]:
        return self.repo.get(id)

    def update(self, id: int, obj_in: ToDoUpdate) -> Optional[ToDoInDB]:
        return self.repo.update(id, obj_in)

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)
