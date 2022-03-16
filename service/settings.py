import os
from sys import argv


if len(argv) > 2 and argv[2] == '--local':
    DB_URL: str = os.environ['DB_URL_LOCAL']
    PORT: str = os.environ['PORT_LOCAL']

else:
    DB_URL: str = os.environ['DB_URL_DOCKER']
    PORT: str = os.environ['PORT_DOCKER']

APP_HOST: str = os.environ['APP_HOST']
