from http import HTTPStatus

from fastapi import APIRouter, Depends
from sas_running.controllers.users import UserController
from sas_running.dependencies import get_user_controller
from sas_running.models.runs import Run
from sas_running.models.users import UserCreate, UserUpdate, User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[User])
def get_users(*, user_controller: UserController = Depends(get_user_controller)):
    return user_controller.get_users()


@router.get("/{user_id}", response_model=User)
def get_user_by_id(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_user_by_id(user_id)


@router.post("/", response_model=User)
def create_user(
    *,
    user_create: UserCreate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.create_user(user_create)


@router.delete("/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    user_controller.delete_user(user_id)


@router.patch("/{user_id}", response_model=User)
def update_user(
    *,
    user_id: int,
    user_update: UserUpdate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.update_user(user_id, user_update)


@router.get("/{user_id}/runs", response_model=list[Run])
def get_user_runs(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_user_runs(user_id)
