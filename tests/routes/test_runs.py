from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from sas_running.controllers.runs import RunController

from sas_running.dependencies import get_run_controller
from sas_running.models.runs import Run


def test_get_runs(run_controller: RunController, app: FastAPI, client: TestClient):
    def _mock_get_runs():
        run_controller.get_runs = Mock(
            return_value=[
                Run(id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1),
                Run(id=2, distance=332.43, time=4300, date="2021-12-31", user_id=1),
                Run(id=3, distance=443.67, time=5200, date="2022-09-30", user_id=1),
            ]
        )
        return run_controller

    app.dependency_overrides[get_run_controller] = _mock_get_runs
    get_runs_response = client.get("/runs/")
    assert get_runs_response.status_code == 200
    assert get_runs_response.json() == [
        {"id": 1, "distance": 245.45, "time": 3000, "date": "2023-11-23", "user_id": 1},
        {"id": 2, "distance": 332.43, "time": 4300, "date": "2021-12-31", "user_id": 1},
        {"id": 3, "distance": 443.67, "time": 5200, "date": "2022-09-30", "user_id": 1},
    ]


def test_get_run_by_id(run_controller: RunController, app: FastAPI, client: TestClient):
    def _mock_get_run_by_id():
        run_controller.get_run_by_id = Mock(
            return_value=Run(
                id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1
            )
        )
        return run_controller

    app.dependency_overrides[get_run_controller] = _mock_get_run_by_id
    get_run_by_id_response = client.get("/runs/1")
    assert get_run_by_id_response.status_code == 200
    assert get_run_by_id_response.json() == {
        "id": 1,
        "distance": 245.45,
        "time": 3000,
        "date": "2023-11-23",
        "user_id": 1,
    }


def test_create_run(run_controller: RunController, app: FastAPI, client: TestClient):
    def _mock_create_run():
        run_controller.create_run = Mock(
            return_value=Run(
                id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1
            )
        )
        return run_controller

    app.dependency_overrides[get_run_controller] = _mock_create_run
    create_run_response = client.post(
        "/runs/",
        json={"distance": 245.45, "time": 3000, "date": "2023-11-23", "user_id": 1},
    )
    assert create_run_response.status_code == 200
    assert create_run_response.json() == {
        "id": 1,
        "distance": 245.45,
        "time": 3000,
        "date": "2023-11-23",
        "user_id": 1,
    }


def test_delete_run(run_controller: RunController, app: FastAPI, client: TestClient):
    def _mock_delete_run():
        run_controller.delete_run = Mock(
            return_value=Run(
                id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1
            )
        )
        return run_controller

    app.dependency_overrides[get_run_controller] = _mock_delete_run
    delete_run_response = client.delete("/runs/1")
    assert delete_run_response.status_code == 204


def test_update_run(run_controller: RunController, app: FastAPI, client: TestClient):
    def _mock_update_run():
        run_controller.update_run = Mock(
            return_value=Run(
                id=1, distance=245.45, time=3000, date="2023-11-23", user_id=1
            )
        )
        return run_controller

    app.dependency_overrides[get_run_controller] = _mock_update_run
    update_run_response = client.patch(
        "/runs/1", json={"distance": 245.45, "time": 3000, "date": "2023-11-23"}
    )
    assert update_run_response.status_code == 200
    assert update_run_response.json() == {
        "id": 1,
        "distance": 245.45,
        "time": 3000,
        "date": "2023-11-23",
        "user_id": 1,
    }
