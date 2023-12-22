from datetime import date
from enum import Enum
from sqlmodel import Field, SQLModel


class Gender(Enum):
    MEN = "men"
    WOMEN = "women"
    OTHER = "other"


class UserBase(SQLModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: Gender


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
