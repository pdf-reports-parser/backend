import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    DB_URL: str
    APP_PORT: str
    APP_HOST: str


def load_from_env() -> AppConfig:
    return AppConfig(
        DB_URL=os.environ['DB_URL'],
        APP_PORT=os.environ['APP_PORT'],
        APP_HOST=os.environ['APP_HOST'],
    )
