from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class ToDoTagLink(SQLModel, table=True):
    todo_id: Optional[int] = Field(default=None, foreign_key="todo.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    todos: List["ToDo"] = Relationship(back_populates="tags", link_model=ToDoTagLink)


class ToDo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    is_done: bool = False
    due_date: Optional[datetime] = None
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    tags: List[Tag] = Relationship(back_populates="todos", link_model=ToDoTagLink)
    owner: Optional["User"] = Relationship(back_populates="todos", sa_relationship_kwargs={"lazy":"selectin"})


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    todos: List[ToDo] = Relationship(back_populates="owner")


# relationships configured via class attributes
