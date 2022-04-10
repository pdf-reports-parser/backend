import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    db_url: str
    app_port: str
    app_host: str
    track_modifications: bool


def load_from_env() -> AppConfig:
    return AppConfig(
        db_url=os.environ['DB_URL'],
        app_port=os.environ['APP_PORT'],
        app_host=os.environ['APP_HOST'],
        track_modifications=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False'),
    )
