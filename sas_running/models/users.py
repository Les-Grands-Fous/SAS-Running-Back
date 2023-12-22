from uuid import UUID
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int
    sex: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    sex: str


class UserUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
