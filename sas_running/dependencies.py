from fastapi import Depends
from sqlmodel import Session

from sas_running.controllers.users import UserController
from sas_running.database import engine


def get_session():
    with Session(engine) as session:
        yield session


def get_user_controller(session=Depends(get_session)):
    return UserController(session)
