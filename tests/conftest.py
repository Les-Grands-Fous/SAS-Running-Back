import pytest
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from sas_running.controllers.runs import RunController
from sas_running.controllers.users import UserController


@pytest.fixture(name="engine")
def fixture_engine():
    sqlite_url = "sqlite://"
    engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture(name="session")
def fixture_session(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture(name="user_controller")
def fixture_user_controller(session):
    return UserController(session)


@pytest.fixture(name="run_controller")
def fixture_run_controller(session):
    return RunController(session)
