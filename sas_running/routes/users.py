from fastapi import APIRouter, Depends
from sas_running.controllers.users import UserController
from sas_running.dependencies import get_user_controller
from sas_running.models.users import UserCreate, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_users(*, user_controller: UserController = Depends(get_user_controller)):
    return user_controller.get_users()


@router.get("/{user_id}")
def get_user_by_id(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_user_by_id(user_id)


@router.post("/")
def create_user(
    *,
    user_create: UserCreate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.create_user(user_create)


@router.delete("/{user_id}")
def delete_user(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    user_controller.delete_user(user_id)


@router.patch("/{user_id}")
def update_user(
    *,
    user_id: int,
    user_update: UserUpdate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.update_user(user_id, user_update)
