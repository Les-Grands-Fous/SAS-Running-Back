import datetime
from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from sas_running.controllers.users import UserController
from sas_running.dependencies import get_user_controller
from sas_running.models.runs import Run
from sas_running.models.users import User, Gender


def test_get_users(user_controller: UserController, app: FastAPI, client: TestClient):
    def _mock_get_users():
        user_controller.get_users = Mock(
            return_value=[
                User(
                    id=1,
                    first_name="Samira",
                    last_name="Souhib",
                    birth_date=datetime.date(2023, 10, 14),
                    gender=Gender.WOMAN,
                ),
                User(
                    id=2,
                    first_name="Poppy",
                    last_name="Iona",
                    birth_date=datetime.date(2022, 8, 11),
                    gender=Gender.WOMAN,
                ),
                User(
                    id=3,
                    first_name="Garen",
                    last_name="Demacia",
                    birth_date=datetime.date(2008, 7, 21),
                    gender=Gender.OTHER,
                ),
            ]
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_users
    get_users_response = client.get("/users/")
    assert get_users_response.status_code == 200
    assert get_users_response.json() == [
        {
            "id": 1,
            "first_name": "Samira",
            "last_name": "Souhib",
            "birth_date": "2023-10-14",
            "gender": "woman",
        },
        {
            "id": 2,
            "first_name": "Poppy",
            "last_name": "Iona",
            "birth_date": "2022-08-11",
            "gender": "woman",
        },
        {
            "id": 3,
            "first_name": "Garen",
            "last_name": "Demacia",
            "birth_date": "2008-07-21",
            "gender": "other",
        },
    ]


def test_get_user_by_id(
    user_controller: UserController, app: FastAPI, client: TestClient
):
    def _mock_get_user_by_id():
        user_controller.get_user_by_id = Mock(
            return_value=User(
                id=1,
                first_name="Samira",
                last_name="Souhib",
                birth_date=datetime.date(2023, 10, 14),
                gender=Gender.WOMAN,
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_user_by_id
    get_user_by_id_response = client.get("/users/1")
    assert get_user_by_id_response.status_code == 200
    assert get_user_by_id_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "birth_date": "2023-10-14",
        "gender": "woman",
    }


def test_create_user(user_controller: UserController, app: FastAPI, client: TestClient):
    def _mock_create_user():
        user_controller.create_user = Mock(
            return_value=User(
                id=1,
                first_name="Samira",
                last_name="Souhib",
                birth_date=datetime.date(2023, 10, 14),
                gender=Gender.WOMAN,
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_create_user
    create_user_response = client.post(
        "/users/",
        json={
            "first_name": "Samira",
            "last_name": "Souhib",
            "birth_date": "2023-10-14",
            "gender": "woman",
        },
    )
    assert create_user_response.status_code == 200
    assert create_user_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "birth_date": "2023-10-14",
        "gender": "woman",
    }


def test_delete_user(user_controller: UserController, app: FastAPI, client: TestClient):
    def _mock_delete_user():
        user_controller.delete_user = Mock(
            return_value=User(
                id=1,
                first_name="Samira",
                last_name="Souhib",
                birth_date=datetime.date(2023, 10, 14),
                gender=Gender.WOMAN,
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_delete_user
    delete_user_response = client.delete("/users/1")
    assert delete_user_response.status_code == 204


def test_update_user(user_controller: UserController, app: FastAPI, client: TestClient):
    def _mock_update_user():
        user_controller.update_user = Mock(
            return_value=User(
                id=1,
                first_name="Samira",
                last_name="Souhib",
                birth_date=datetime.date(2023, 10, 14),
                gender=Gender.WOMAN,
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_update_user
    update_user_response = client.patch(
        "/users/1",
        json={
            "first_name": "Samira",
            "last_name": "Souhib",
            "birth_date": "2023-10-14",
            "gender": "woman",
        },
    )
    assert update_user_response.status_code == 200
    assert update_user_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "birth_date": "2023-10-14",
        "gender": "woman",
    }


def test_get_user_runs(
    user_controller: UserController, app: FastAPI, client: TestClient
):
    def _mock_get_user_runs():
        user_controller.get_user_runs = Mock(
            return_value=[
                Run(id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1),
                Run(id=2, distance=332.43, time=4300, date="2021-12-31", user_id=1),
                Run(id=3, distance=443.67, time=5200, date="2022-09-30", user_id=1),
            ]
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_user_runs
    get_user_runs_response = client.get("/users/1/runs")
    assert get_user_runs_response.status_code == 200
    assert get_user_runs_response.json() == [
        {"id": 1, "distance": 245.45, "time": 3000, "date": "2023-11-23", "user_id": 1},
        {"id": 2, "distance": 332.43, "time": 4300, "date": "2021-12-31", "user_id": 1},
        {"id": 3, "distance": 443.67, "time": 5200, "date": "2022-09-30", "user_id": 1},
    ]
