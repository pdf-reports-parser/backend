import os

# default value
RUN_TYPE = 'docker'

DB_URL = {
    'docker': os.environ['DB_URL_DOCKER'],
    'local': os.environ['DB_URL_LOCAL'],
}

PORT = {
    'docker': os.environ['PORT_DOCKER'],
    'local': os.environ['PORT_LOCAL'],
}

APP_HOST = os.environ['APP_HOST']
