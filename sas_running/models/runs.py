from sqlmodel import SQLModel, Field
from datetime import date


class RunBase(SQLModel):
    distance: float
    time: int
    date: date


class Run(RunBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")


class RunCreate(RunBase):
    user_id: int


class RunUpdate(RunBase):
    pass
