from datetime import datetime
from http import HTTPStatus
import logging

from flask import Blueprint, jsonify, request

from service.db import db_session
from service.models import Measurements
from service.settings import TIME_FORMAT

measure = Blueprint('measure', __name__)


@measure.get('/')
def get_measurements():
    query_measure = Measurements.query.all()
    measurement = [row.as_dict() for row in query_measure]
    logging.debug(measurement)
    return jsonify(measurement)


@measure.get('/<uid>')
def get_by_id(uid):
    measurement = Measurements.query.filter_by(id=uid)
    logging.debug(uid)
    logging.debug(measurement)
    if not list(measurement):
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    return measurement[0].as_dict()


@measure.post('/')
def add_measurement():
    measurement = request.json
    input_measure = Measurements(
        name=measurement['name'],
        status=measurement['status'],
        description=measurement['description'],
        measure_time=datetime.strptime(measurement['measure_time'], TIME_FORMAT),
        test_id=measurement['test_id'],
    )
    db_session.add(input_measure)
    db_session.commit()
    return measurement, HTTPStatus.CREATED


@measure.put('/<uid>')
def update_measurement(uid):
    measurement = Measurements.query.filter_by(id=uid)
    if not list(measurement):
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND
    changes = request.json
    logging.debug(measurement[0].as_dict())
    logging.debug(changes['name'])
    measurement[0].name = changes['name']
    measurement[0].status = changes['status']
    measurement[0].description = changes['status']
    measurement[0].measure_time = changes['measure_time']
    measurement[0].test_id = changes['test_id']
    db_session.commit()
    return changes, HTTPStatus.OK


@measure.delete('/<uid>')
def delete_measurement(uid):
    measurement = Measurements.query.filter_by(id=uid)
    if not list(measurement):
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND
    logging.debug(measurement[0].as_dict())
    measurement.delete()
    db_session.commit()
    return {}, HTTPStatus.NO_CONTENT
