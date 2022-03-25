from http import HTTPStatus
from flask import Blueprint, jsonify, request

from uuid import uuid4

# Temporary dictory of measurements
measurements_storage = {
    'f9cad67d02694fae947dd9bbfe5b9399': {'uid': 'f9cad67d02694fae947dd9bbfe5b9399', 'name': 'Measurement1', 'Data': 'Done'},
    '46debfb4f9e44e1d831f0791d711deb7': {'uid': '46debfb4f9e44e1d831f0791d711deb7', 'name': 'Measurement2', 'Data': 'Permissible'},
    '32235e10f04440bba88db5861b2faeba': {'uid': '32235e10f04440bba88db5861b2faeba', 'name': 'Measurement3', 'Data': 'Failed'}
}


measurement = Blueprint('measurement', __name__)


@measurement.get('/')
def get_measurements():
    measurements = [measurement for _, measurement in measurements_storage.items()]
    return jsonify(measurements)


@measurement.get('/<uid>')
def get_measurement_by_id(uid):
    measurement = measurements_storage.get(uid)
    if not measurement:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND
    return measurement


@measurement.post('/')
def add_measurement():
    measurement = request.json
    measurement['uid'] = uuid4().hex
    measurements_storage[measurement['uid']] = measurement
    return measurement, HTTPStatus.CREATED


@measurement.put('/<uid>')
def update_measurement(uid):
    if uid not in measurements_storage:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND
    # TODO: validation
    measurements_storage[uid] = request.json
    return request.json, HTTPStatus.OK


@measurement.delete('/<uid>')
def delete_measurement(uid):
    if uid not in measurements_storage:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND
    measurements_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT
