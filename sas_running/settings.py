from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="SAS_RUNNING_BACK_", case_sensitive=False)
    host: str
    port: str
    db_name: str
    db_user: str
    db_password: str
    env: str
