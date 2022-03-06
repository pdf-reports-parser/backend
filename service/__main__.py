import logging

from flask import Flask

from service.measurements import measure
from service.models import create_model

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

if __name__ == '__main__':
    create_model()
    app.register_blueprint(measure, url_prefix='/api/v1/measurements')
    app.run(host='0.0.0.0', port=8080)
