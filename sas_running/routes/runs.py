from http import HTTPStatus

from fastapi import Depends, APIRouter
from sas_running.controllers.runs import RunController
from sas_running.dependencies import get_run_controller
from sas_running.models.runs import RunCreate, RunUpdate, Run

router = APIRouter(
    prefix="/runs",
    tags=["runs"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Run])
def get_runs(*, run_controller: RunController = Depends(get_run_controller)):
    return run_controller.get_runs()


@router.get("/{run_id}", response_model=Run)
def get_run_by_id(
    *, run_id: int, run_controller: RunController = Depends(get_run_controller)
):
    return run_controller.get_run_by_id(run_id)


@router.post("/", response_model=Run)
def create_run(
    *,
    run_create: RunCreate,
    run_controller: RunController = Depends(get_run_controller)
):
    return run_controller.create_run(run_create)


@router.delete("/{run_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_run(
    *, run_id: int, run_controller: RunController = Depends(get_run_controller)
):
    run_controller.delete_run(run_id)


@router.patch("/{run_id}")
def update_run(
    *,
    run_id: int,
    run_update: RunUpdate,
    run_controller: RunController = Depends(get_run_controller)
):
    return run_controller.update_run(run_id, run_update)
