import uvicorn
from sas_running.api import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
