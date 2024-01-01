from datetime import date
from enum import Enum
from sqlmodel import Field, SQLModel


class Gender(Enum):
    MAN = "man"
    WOMAN = "woman"
    OTHER = "other"


class UserBase(SQLModel):
    first_name: str
    last_name: str
    birth_date: date | None = None
    gender: Gender | None = None


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
