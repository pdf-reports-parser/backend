from http import HTTPStatus
from uuid import uuid4

from flask import Flask, jsonify, request


measurement_storage = {
    "e7b3d405ac9a45758109f3daee0adfae": {
        "uid": "e7b3d405ac9a45758109f3daee0adfae",
        "test_uid": "1",
        "name": "7.1.2 Overall Delay in SND DVNB",
        "status": "Done",
        "description": "GOST 33468-NB Rev.04 \ Hands-free Parameters \ Delay Measurements (DVNB) \ SND Direction",
        "time": "06.12.2021 14:57",
    },
    "3074db5ea6064b75b5c8e13d0415a4e3": {
        "uid": "3074db5ea6064b75b5c8e13d0415a4e3",
        "test_uid": "1",
        "name": "7.1.2 Calc: Delay SND DUT GSM DVNB",
        "status": "Ok",
        "description": "GOST 33468-NB Rev.04 \ Hands-free Parameters \ Delay Measurements (DVNB) \ SND Direction",
        "time": "06.12.2021 14:58",
    },
}

app = Flask(__name__)


@app.get('/api/v1/measurements/')
def get_measurements():
    measurements = [measurment for _, measurment in measurement_storage.items()]
    return jsonify(measurements)


@app.get('/api/v1/measurements/<uid>')
def get_by_id(uid):
    measurment = measurement_storage.get(uid)
    if not measurment:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    return measurment


@app.post('/api/v1/measurements/')
def add_measurement():
    measurement = request.json
    measurement['uid'] = uuid4().hex
    measurement_storage[measurement['uid']] = measurement
    return measurement, HTTPStatus.CREATED


@app.put('/api/v1/measurements/<uid>')
def update_measurement(uid):
    if uid not in measurement_storage:
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND
    measurment = request.json
    measurement_storage[uid] = measurment
    return measurment, HTTPStatus.OK


@app.delete('/api/v1/measurements/<uid>')
def delete_measurement(uid):
    if uid not in measurement_storage:
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND
    measurement_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
