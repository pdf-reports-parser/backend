from flask import Flask

from service.views.measurements import measure


def create_app():
    app = Flask(__name__)

    app.register_blueprint(measure, url_prefix='/api/v1/measurements')

    return app
