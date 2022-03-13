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
    measurement = schemas.Measurement.from_orm(entity)
    return measurement.dict(), HTTPStatus.OK


@measure.post('/')
def add_measurement():
    payload = request.json
    payload['uid'] = -1
    measurement = schemas.Measurement(**payload)
    entity = repo.add(
        name=measurement.name,
        status=measurement.status,
        description=measurement.description,
        measure_time=measurement.measure_time,
        test_id=measurement.test_id,
    )
    new_measurement = schemas.Measurement.from_orm(entity)
    return new_measurement.dict(), HTTPStatus.CREATED


@measure.put('/<uid>')
def update_measurement(uid: int):
    payload = request.json
    payload['uid'] = uid

    measurement = schemas.Measurement(**payload)
    entity = repo.update(
        uid=uid,
        name=measurement.name,
        status=measurement.status,
        description=measurement.description,
        measure_time=measurement.measure_time,
        test_id=measurement.test_id,
    )

    if not entity:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND

    fresh_measurement = schemas.Measurement.from_orm(entity)
    return fresh_measurement.dict(), HTTPStatus.OK


@measure.delete('/<uid>')
def delete_measurement(uid: int):
     repo.delete(uid)
     return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
