from http import HTTPStatus

from flask import Blueprint, jsonify, request

from service.repos.measurements import MeasurementsRepo

measure = Blueprint('measure', __name__)

repo = MeasurementsRepo()


@measure.get('/')
def get_measurements():
    return jsonify(repo.get_all())


@measure.get('/<uid>')
def get_by_id(uid: int):
    measurement: dict = repo.get_by_uid(uid)
    if measurement:
        return measurement
    return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND


@measure.post('/')
def add_measurement():
    measurement = request.json
    repo.add(
        name=measurement['name'],
        status=measurement['status'],
        description=measurement['description'],
        measure_time=measurement['measure_time'],
        test_id=measurement['test_id'],
    )
    return measurement, HTTPStatus.CREATED


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
