from sqlalchemy import create_engine
from sqlmodel import SQLModel

from sas_running.settings import Settings

settings = Settings()
sqlite_file_name = "database.db"
sqlite_url = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.host}:{settings.port}/{settings.db_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
