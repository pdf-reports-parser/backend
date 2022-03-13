from http import HTTPStatus

from flask import Flask
from pydantic import ValidationError
from werkzeug.exceptions import HTTPException

from service.errors import AppError
from service.views.measurements import measure


def handle_http_exceptions(error: HTTPException):
    return {'message': error.description}, error.code


def handle_app_error(error: AppError):
    return {'message': error.reason}, error.status


def handle_validation_error(error: ValidationError):
    return error.json(), HTTPStatus.BAD_REQUEST


def create_app():
    app = Flask(__name__)

    app.register_blueprint(measure, url_prefix='/api/v1/measurements')

    app.register_error_handler(HTTPException, handle_http_exceptions)
    app.register_error_handler(AppError, handle_app_error)
    app.register_error_handler(ValidationError, handle_validation_error)

    return app
