from http import HTTPStatus
from typing import Any, Optional

import orjson
from flask import Blueprint, abort, request

from service import schemas
from service.repos.measurements import MeasurementsRepo

measurement_view = Blueprint('measurement_view', __name__)

repo = MeasurementsRepo()


@measurement_view.get('/')
def get_measurements():
    entities = repo.get_all()
    measurements = [schemas.Measurement.from_orm(entity).dict() for entity in entities]
    return orjson.dumps(measurements), HTTPStatus.OK


@measurement_view.get('/<uid>')
def get_measurement_by_id(uid: int):
    entity = repo.get_by_uid(uid)
    if not entity:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND
    measurement = schemas.Measurement.from_orm(entity)
    return measurement.dict(), HTTPStatus.OK


@measurement_view.post('/')
def add_measurement():
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'The body of the request could not be empty')

    payload['uid'] = -1

    measurement = schemas.Measurement(**payload)
    entity = repo.add(
        measurement_object=measurement.measurement_object,
        project=measurement.project,
        report_date=measurement.report_date,
        responsible_person=measurement.responsible_person,
    )

    new_measurement = schemas.Measurement.from_orm(entity)
    return new_measurement.dict(), HTTPStatus.CREATED


@measurement_view.put('/<uid>')
def update_measurement(uid: int):
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'The body of the request could not be empty')

    payload['uid'] = uid

    measurement = schemas.Measurement(**payload)
    entity = repo.update(
        uid=uid,
        measurement_object=measurement.measurement_object,
        project=measurement.project,
        report_date=measurement.report_date,
        responsible_person=measurement.responsible_person,
    )

    if not entity:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND

    fresh_measurement = schemas.Measurement.from_orm(entity)
    return fresh_measurement.dict(), HTTPStatus.OK


@measurement_view.delete('/<uid>')
def delete_measurement(uid: int):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
