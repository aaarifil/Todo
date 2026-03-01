from datetime import datetime
from threading import Lock
from typing import List, Optional
from schemas.todo import ToDoInDB, ToDoCreate, ToDoUpdate


class ToDoRepository:
    def __init__(self):
        self._items: List[ToDoInDB] = []
        self._lock = Lock()
        self._next_id = 1

    def create(self, obj_in: ToDoCreate) -> ToDoInDB:
        with self._lock:
            now = datetime.utcnow()
            item = ToDoInDB(
                id=self._next_id,
                title=obj_in.title,
                description=obj_in.description,
                is_done=obj_in.is_done,
                created_at=now,
                updated_at=now,
            )
            self._items.append(item)
            self._next_id += 1
            return item

    def list(self) -> List[ToDoInDB]:
        return list(self._items)

    def get(self, id: int) -> Optional[ToDoInDB]:
        for it in self._items:
            if it.id == id:
                return it
        return None

    def update(self, id: int, obj_in: ToDoUpdate) -> Optional[ToDoInDB]:
        with self._lock:
            item = self.get(id)
            if not item:
                return None
            if obj_in.title is not None:
                item.title = obj_in.title
            if obj_in.description is not None:
                item.description = obj_in.description
            if obj_in.is_done is not None:
                item.is_done = obj_in.is_done
            item.updated_at = datetime.utcnow()
            return item

    def delete(self, id: int) -> bool:
        with self._lock:
            item = self.get(id)
            if not item:
                return False
            self._items.remove(item)
            return True

    def filter_sort_paginate(
        self,
        is_done: Optional[bool] = None,
        q: Optional[str] = None,
        sort: str = "created_at",
        limit: int = 10,
        offset: int = 0,
    ):
        items = list(self._items)
        if is_done is not None:
            items = [i for i in items if i.is_done == is_done]
        if q:
            qq = q.lower()
            items = [i for i in items if qq in (i.title or "").lower()]
        reverse = False
        key = "created_at"
        if sort.startswith("-"):
            reverse = True
            key = sort[1:]
        else:
            key = sort

        if key == "created_at":
            items.sort(key=lambda x: x.created_at, reverse=reverse)

        total = len(items)
        items_page = items[offset : offset + limit]
        return items_page, total
