from http import HTTPStatus

from flask import Flask
from pydantic import ValidationError
from werkzeug.exceptions import HTTPException

from service.db import db_session
from service.errors import AppError
from service.views.measurements import measurement_view
from service.views.trials import trial_view
from service.views.upload import upload


def handle_http_exceptions(error: HTTPException):
    return {'message': error.description}, error.code


def handle_app_error(error: AppError):
    return {'message': error.reason}, error.status


def handle_validation_error(error: ValidationError):
    return error.json(), HTTPStatus.BAD_REQUEST


def shutdown_session(exception=None):
    db_session.remove()


def create_app():
    app = Flask(__name__)

    app.register_blueprint(trial_view, url_prefix='/api/v1/trials')
    app.register_blueprint(measurement_view, url_prefix='/api/v1/measurements')
    app.register_blueprint(upload, url_prefix='/api/v1/measurements/upload')

    app.register_error_handler(HTTPException, handle_http_exceptions)
    app.register_error_handler(AppError, handle_app_error)
    app.register_error_handler(ValidationError, handle_validation_error)

    app.teardown_appcontext(shutdown_session)

    return app
