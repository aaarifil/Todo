from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class ToDoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    is_done: bool = False

    @validator("title")
    def non_empty_title(cls, v: str):
        if not v.strip():
            raise ValueError("title must not be empty or whitespace")
        return v


class ToDoCreate(ToDoBase):
    pass


class ToDoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    is_done: Optional[bool] = None


class ToDoInDB(ToDoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ToDoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_done: bool
    created_at: datetime
    updated_at: datetime


class ToDoListResponse(BaseModel):
    items: list[ToDoResponse]
    total: int
    limit: int
    offset: int
