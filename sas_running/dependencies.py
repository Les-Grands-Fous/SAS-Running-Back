from fastapi import Depends
from sqlmodel import Session

from sas_running.controllers.runs import RunController
from sas_running.controllers.users import UserController


def get_session():
    from sas_running.database import engine
    with Session(engine) as session:
        yield session


def get_user_controller(session=Depends(get_session)):
    return UserController(session)


def get_run_controller(session=Depends(get_session)):
    return RunController(session)
