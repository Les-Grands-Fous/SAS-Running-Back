from fastapi import FastAPI
from sas_running.routes.users import router as user_router
from sas_running.routes.runs import router as run_router


def create_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(run_router)
    return app
