import logging

from flask import Flask

from service.measurements import measure

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(measure, url_prefix='/api/v1/measurements')
    app.run(host='0.0.0.0', port=8080)