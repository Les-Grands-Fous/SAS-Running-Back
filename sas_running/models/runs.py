from sqlmodel import SQLModel, Field
from datetime import date


class RunBase(SQLModel):
    distance: float
    time: int
    date: date


class Run(RunBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.id")


class RunCreate(RunBase):
    pass


class RunUpdate(RunBase):
    pass
