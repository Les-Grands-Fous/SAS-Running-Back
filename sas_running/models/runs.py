from sqlmodel import SQLModel, Field
from datetime import date


class RunBase(SQLModel):
    distance: float
    time: int
    date: date


class Run(RunBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RunCreate(RunBase):
    pass


class RunUpdate(RunBase):
    pass
