import logging
from http import HTTPStatus

from flask import Blueprint, jsonify, request

from service import schemas
from service.repos.measurements import MeasurementsRepo

measure = Blueprint('measure', __name__)

repo = MeasurementsRepo()


@measure.get('/')
def get_measurements():
    entities = repo.get_all()
    measurements = [schemas.Measurement.from_orm(entity).dict() for entity in entities]
    return jsonify(measurements), HTTPStatus.OK


@measure.get('/<uid>')
def get_by_id(uid: int):
    entity = repo.get_by_uid(uid)
    if not entity:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    measurement = schemas.Measurement.from_orm(entity).dict()
    return measurement

@measure.post('/')
def add_measurement():
    measurement = schemas.Measurement(**request.json)
    entity = repo.add(**measurement.dict())
    new_measurement = schemas.Measurement.from_orm(entity)
    return new_measurement.dict(), HTTPStatus.CREATED


@measure.put('/<uid>')
def update_measurement(uid: int):
    changes = request.json
    measure_update = repo.update(
        uid=uid,
        name=changes['name'],
        status=changes['status'],
        description=changes['description'],
        measure_time=changes['measure_time'],
        test_id=changes['test_id'],
    )
    if measure_update:
        return changes, HTTPStatus.OK
    return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND


@measure.delete('/<uid>')
def delete_measurement(uid: int):
    if repo.delete(uid):
        return {}, HTTPStatus.NO_CONTENT
    return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
