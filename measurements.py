from flask import Flask, jsonify, request
from http import HTTPStatus
from uuid import uuid4

measurment_storage = {
    "e7b3d405ac9a45758109f3daee0adfae": {
        "uid": "e7b3d405ac9a45758109f3daee0adfae",
        "test_uid": "1",
        "name": "7.1.2 Overall Delay in SND DVNB",
        "status": "Done",
        "descriotion": "GOST 33468-NB Rev.04 \ Hands-free Parameters \ Delay Measurements (DVNB) \ SND Direction",
        "time": "06.12.2021 14:57",
    },
    "3074db5ea6064b75b5c8e13d0415a4e3": {
        "uid": "3074db5ea6064b75b5c8e13d0415a4e3",
        "test_uid": "1",
        "name": "7.1.2 Calc: Delay SND DUT GSM DVNB",
        "status": "Ok",
        "descriotion": "GOST 33468-NB Rev.04 \ Hands-free Parameters \ Delay Measurements (DVNB) \ SND Direction",
        "time": "06.12.2021 14:58",
    },
}


app = Flask(__name__)

@app.get('/api/measurements/')
def get_measurements():
    measurements = [
        measurment for _, measurment in measurment_storage.items()
    ]
    return jsonify(measurements)


@app.get('/api/measurements/<uid>')
def get_by_id(uid):
    measurment = measurment_storage.get(uid)
    if not measurment:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    return measurment


@app.post('/api/measurements/')
def add_measurement():
    measurment = request.json
    measurment['uid'] = uuid4().hex
    measurment_storage[measurment['uid']] = measurment
    return measurment, HTTPStatus.CREATED


@app.put('/api/measurements/<uid>')
def update_measurement(uid):
    if uid not in measurment_storage:
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND

    measurment = request.json
    # TODO: validation skipped

    measurment_storage[uid] = measurment
    return measurment, HTTPStatus.OK


@app.delete('/api/measurements/<uid>')
def delete_measurement(uid):
    if uid not in measurment_storage:
        return {"message": "measurment not found"}, HTTPStatus.NOT_FOUND
    measurment_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT


