from fastapi import Depends, APIRouter
from sas_running.controllers.runs import RunController
from sas_running.dependencies import get_run_controller
from sas_running.models.runs import RunCreate, RunUpdate

router = APIRouter(
    prefix="/runs",
    tags=["runs"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_runs(*, run_controller: RunController = Depends(get_run_controller)):
    return run_controller.get_runs()


@router.get("/{run_id}")
def get_run_by_id(
    *, user_id: int, run_controller: RunController = Depends(get_run_controller)
):
    return run_controller.get_run_by_id(user_id)


@router.post("/")
def create_run(
    *,
    run_create: RunCreate,
    run_controller: RunController = Depends(get_run_controller)
):
    return run_controller.create_run(run_create)


@router.delete("/{run_id}")
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
