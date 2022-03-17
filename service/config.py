import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    DB_URL = os.environ['DB_URL']

    APP_PORT = os.environ['APP_PORT']

    APP_HOST = os.environ['APP_HOST']
