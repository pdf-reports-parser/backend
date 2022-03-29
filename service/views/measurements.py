from http import HTTPStatus
from pathlib import Path
from uuid import uuid4

from flask import Blueprint, abort, jsonify, request
from werkzeug.utils import secure_filename

# Temporary dictory of measurements
measurements_storage = {
    'f9cad67d02694fae947dd9bbfe5b9399': {'uid': 'f9cad67d02694fae947dd9bbfe5b9399', 'name': 'Measurement1', 'Data': 'Done'},  # noqa: E501
    '46debfb4f9e44e1d831f0791d711deb7': {'uid': '46debfb4f9e44e1d831f0791d711deb7', 'name': 'Measurement2', 'Data': 'Permissible'},  # noqa: E501
    '32235e10f04440bba88db5861b2faeba': {'uid': '32235e10f04440bba88db5861b2faeba', 'name': 'Measurement3', 'Data': 'Failed'},  # noqa: E501
}


measurement = Blueprint('measurement', __name__)


@measurement.get('/')
def get_measurements():
    measurements = [measurement for _, measurement in measurements_storage.items()]
    return jsonify(measurements)


@measurement.get('/<uid>')
def get_measurement_by_id(uid):
    measurement_entity = measurements_storage.get(uid)
    if not measurement_entity:
        return {'message': 'measurement not found'}, HTTPStatus.NOT_FOUND
    return measurement


@measurement.post('/')
def add_measurement():
    measurement_entity = request.json
    measurement_entity['uid'] = uuid4().hex
    measurements_storage[measurement_entity['uid']] = measurement_entity
    return measurement_entity, HTTPStatus.CREATED


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


@measurement.route('/download', methods=['GET', 'POST'])
def download_file():
    upload_dir = Path('service/tmp')
    upload_file = upload_dir / 'report.pdf'

    if request.method == 'POST':
        if 'file' not in request.files:
            abort(HTTPStatus.BAD_REQUEST, 'В теле запроса должен передоваться файл ("file")')
        file = request.files['file']
        if not file.filename:
            abort(HTTPStatus.BAD_REQUEST, 'В теле запроса должен передоваться файл ("file")')
        filename = secure_filename(file.filename)
        if Path(filename).suffix != '.pdf':
            abort(HTTPStatus.BAD_REQUEST, 'Неподдерживаемый формат файла - необходим PDF')
        file.save(upload_file)

        return {}, HTTPStatus.ACCEPTED
