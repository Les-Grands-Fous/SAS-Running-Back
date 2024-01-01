import datetime
from sqlmodel import Session, select

from sas_running.controllers.runs import RunController
from sas_running.controllers.users import UserController
from sas_running.models.runs import RunCreate
from sas_running.models.users import UserCreate, Gender, User, UserUpdate


def test_create_user(user_controller: UserController, session: Session):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    users = session.exec(select(User)).all()
    assert len(users) == 1
    assert created_user.first_name == users[0].first_name
    assert created_user.last_name == users[0].last_name
    assert created_user.birth_date == users[0].birth_date
    assert created_user.gender == users[0].gender


def test_get_user_by_id(user_controller: UserController):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    user = user_controller.get_user_by_id(created_user.id)
    assert user.id == created_user.id
    assert user.first_name == created_user.first_name
    assert user.last_name == created_user.last_name
    assert user.birth_date == created_user.birth_date
    assert user.gender == created_user.gender


def test_get_users(user_controller: UserController):
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

    current_date_3 = datetime.date(2023, 8, 20)
    created_user_3 = user_controller.create_user(
        UserCreate(
            first_name="Sivir",
            last_name="Shurima",
            birth_date=current_date_3,
            gender=Gender.WOMAN,
        )
    )
    users = user_controller.get_users()
    assert users[0].first_name == created_user_1.first_name
    assert users[0].last_name == created_user_1.last_name
    assert users[0].birth_date == created_user_1.birth_date
    assert users[0].gender == created_user_1.gender
    assert users[1].first_name == created_user_2.first_name
    assert users[1].last_name == created_user_2.last_name
    assert users[1].birth_date == created_user_2.birth_date
    assert users[1].gender == created_user_2.gender
    assert users[2].first_name == created_user_3.first_name
    assert users[2].last_name == created_user_3.last_name
    assert users[2].birth_date == created_user_3.birth_date
    assert users[2].gender == created_user_3.gender


def test_delete_create_user(user_controller: UserController, session: Session):
    current_date = datetime.date(2023, 12, 28)
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Philou",
            last_name="Pierre",
            birth_date=current_date,
            gender=Gender.MAN,
        )
    )
    user_controller.delete_user(created_user.id)
    user = session.exec(select(User)).all()
    assert len(user) == 0


def test_update_user(user_controller: UserController, session: Session):
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
    user_controller.update_user(
        created_user.id,
        UserUpdate(
            first_name="Vincent",
            last_name="Briar",
            birth_date=current_date_1,
            gender=Gender.WOMAN,
        ),
    )
    user = session.exec(select(User)).all()
    assert user[0].first_name == "Vincent"
    assert user[0].last_name == "Briar"
    assert user[0].birth_date == current_date_1
    assert user[0].gender == Gender.WOMAN


def test_get_user_runs(
    user_controller: UserController,
    run_controller: RunController,
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
            distance=234.34, time=3600, date=current_date, user_id=created_user.id
        )
    )
    created_run_2 = run_controller.create_run(
        RunCreate(
            distance=434.34, time=6600, date=current_date, user_id=created_user.id
        )
    )
    created_run_3 = run_controller.create_run(
        RunCreate(
            distance=534.34, time=6400, date=current_date, user_id=created_user.id
        )
    )
    created_run_4 = run_controller.create_run(
        RunCreate(
            distance=834.34, time=7600, date=current_date_2, user_id=created_user_2.id
        )
    )
    user1_runs = user_controller.get_user_runs(user_id=created_user.id)
    user2_runs = user_controller.get_user_runs(user_id=created_user_2.id)
    assert len(user1_runs) == 3
    assert len(user2_runs) == 1
    assert user1_runs[0].user_id == created_run_1.user_id
    assert user1_runs[0].distance == created_run_1.distance
    assert user1_runs[0].time == created_run_1.time
    assert user1_runs[0].date == created_run_1.date

    assert user1_runs[1].user_id == created_run_2.user_id
    assert user1_runs[1].distance == created_run_2.distance
    assert user1_runs[1].time == created_run_2.time
    assert user1_runs[1].date == created_run_2.date

    assert user1_runs[2].user_id == created_run_3.user_id
    assert user1_runs[2].distance == created_run_3.distance
    assert user1_runs[2].time == created_run_3.time
    assert user1_runs[2].date == created_run_3.date

    assert user2_runs[0].user_id == created_run_4.user_id
    assert user2_runs[0].distance == created_run_4.distance
    assert user2_runs[0].time == created_run_4.time
    assert user2_runs[0].date == created_run_4.date
