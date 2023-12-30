import datetime
from sqlmodel import Session, select
from sas_running.controllers.runs import RunController
from sas_running.controllers.users import UserController
from sas_running.models.runs import Run, RunCreate, RunUpdate
from sas_running.models.users import UserCreate, Gender


def test_create_run(
    user_controller: UserController, run_controller: RunController, session: Session
):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    created_run = run_controller.create_run(
        RunCreate(
            distance=234.34, time=3600, date=current_date, user_id=created_user.id
        )
    )
    runs = session.exec(select(Run)).one()
    assert created_run.distance == runs.distance
    assert created_run.time == runs.time
    assert created_run.date == runs.date
    assert created_run.user_id == runs.user_id


def test_get_run_by_id(user_controller: UserController, run_controller: RunController):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    created_run_1 = run_controller.create_run(
        RunCreate(
            distance=394.34, time=4200, date=current_date, user_id=created_user.id
        )
    )
    _ = run_controller.create_run(
        RunCreate(
            distance=534.34, time=5400, date=current_date, user_id=created_user.id
        )
    )
    _ = run_controller.create_run(
        RunCreate(
            distance=234.34, time=3600, date=current_date, user_id=created_user.id
        )
    )
    run = run_controller.get_run_by_id(created_run_1.id)
    assert run.id == created_run_1.id
    assert run.distance == created_run_1.distance
    assert run.time == created_run_1.time
    assert run.date == created_run_1.date
    assert run.user_id == created_run_1.user_id


def test_get_runs(user_controller: UserController, run_controller: RunController):
    current_date_1 = datetime.date(2023, 12, 28)
    created_user_1 = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date_1,
            gender=Gender.MAN,
        )
    )

    current_date_2 = datetime.date(2023, 11, 23)
    created_user_2 = user_controller.create_user(
        UserCreate(
            first_name="Tima",
            last_name="Lulu",
            birth_date=current_date_2,
            gender=Gender.WOMAN,
        )
    )
    created_run_1 = run_controller.create_run(
        RunCreate(
            distance=394.34, time=4200, date=current_date_1, user_id=created_user_1.id
        )
    )
    created_run_2 = run_controller.create_run(
        RunCreate(
            distance=534.34, time=5400, date=current_date_1, user_id=created_user_1.id
        )
    )
    created_run_3 = run_controller.create_run(
        RunCreate(
            distance=234.34, time=3600, date=current_date_1, user_id=created_user_1.id
        )
    )
    created_run_4 = run_controller.create_run(
        RunCreate(
            distance=634.34, time=7400, date=current_date_2, user_id=created_user_2.id
        )
    )
    created_run_5 = run_controller.create_run(
        RunCreate(
            distance=134.34, time=2600, date=current_date_2, user_id=created_user_2.id
        )
    )
    runs = run_controller.get_runs()
    assert runs[0].distance == created_run_1.distance
    assert runs[0].time == created_run_1.time
    assert runs[0].date == created_run_1.date
    assert runs[0].user_id == created_run_1.user_id
    assert runs[1].distance == created_run_2.distance
    assert runs[1].time == created_run_2.time
    assert runs[1].date == created_run_2.date
    assert runs[1].user_id == created_run_2.user_id
    assert runs[2].distance == created_run_3.distance
    assert runs[2].time == created_run_3.time
    assert runs[2].date == created_run_3.date
    assert runs[2].user_id == created_run_3.user_id
    assert runs[3].distance == created_run_4.distance
    assert runs[3].time == created_run_4.time
    assert runs[3].date == created_run_4.date
    assert runs[3].user_id == created_run_4.user_id
    assert runs[4].distance == created_run_5.distance
    assert runs[4].time == created_run_5.time
    assert runs[4].date == created_run_5.date
    assert runs[4].user_id == created_run_5.user_id


def test_delete_create_run(
    user_controller: UserController, run_controller: RunController, session: Session
):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    created_run_1 = run_controller.create_run(
        RunCreate(
            distance=394.34, time=4200, date=current_date, user_id=created_user.id
        )
    )
    created_run_2 = run_controller.create_run(
        RunCreate(
            distance=494.34, time=5200, date=current_date, user_id=created_user.id
        )
    )
    run_controller.delete_run(created_run_1.id)
    run = session.exec(select(Run)).one()
    assert run.distance == created_run_2.distance
    assert run.time == created_run_2.time
    assert run.date == created_run_2.date
    assert run.user_id == created_run_2.user_id


def test_update_run(
    user_controller: UserController, run_controller: RunController, session: Session
):
    current_date = datetime.date(2023, 12, 28)
    current_date_1 = datetime.date(2022, 10, 26)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    created_run = run_controller.create_run(
        RunCreate(
            distance=394.34, time=4200, date=current_date, user_id=created_user.id
        )
    )
    updated_run = run_controller.update_run(
        created_run.user_id, RunUpdate(distance=594.34, time=5200, date=current_date_1)
    )
    run = session.exec(select(Run)).all()
    assert run[0].distance == updated_run.distance
    assert run[0].time == updated_run.time
    assert run[0].date == updated_run.date
    assert run[0].user_id == updated_run.user_id
