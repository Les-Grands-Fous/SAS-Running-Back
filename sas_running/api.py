import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sas_running.routes.users import router as user_router


def create_app():
    app = FastAPI()
    app.include_router(user_router)
    return app
