from distutils.log import debug
from flask import Flask, jsonify, request
from http import HTTPStatus
from uuid import uuid4

# Temporary dictory of tests
tests_storage = {
    'f9cad67d02694fae947dd9bbfe5b9399': {'uid': 'f9cad67d02694fae947dd9bbfe5b9399', 'name': 'Test1', 'Data': 'Done'},
    '46debfb4f9e44e1d831f0791d711deb7': {'uid': '46debfb4f9e44e1d831f0791d711deb7', 'name': 'Test2', 'Data': 'Permissible'},
    '32235e10f04440bba88db5861b2faeba': {'uid': '32235e10f04440bba88db5861b2faeba', 'name': 'Test3', 'Data': 'Failed'}
}


app = Flask(__name__)


@app.get('/api/v1/tests/')
def get_tests():
    tests = [test for _, test in tests_storage.items()]
    return jsonify(tests)


@app.get('/api/v1/tests/<uid>')
def get_test_by_id(uid):
    test = tests_storage.get(uid)
    if not test:
        return {'message': 'test not found'}, HTTPStatus.NOT_FOUND
    return test


@app.post('/api/v1/tests/')
def add_test():
    test = request.json
    test['uid'] = uuid4().hex
    tests_storage[test['uid']] = test
    return test, HTTPStatus.CREATED


@app.put('/api/v1/tests/<uid>')
def update_test(uid):
    if uid not in tests_storage:
        return {'message': 'test not found'}, HTTPStatus.NOT_FOUND
    # TODO: validation
    tests_storage[uid] = request.json
    return request.json, HTTPStatus.OK


@app.delete('/api/v1/tests/<uid>')
def delete_test(uid):
    if uid not in tests_storage:
        return {'message': 'test not found'}, HTTPStatus.NOT_FOUND
    tests_storage.pop(uid)
    return {}, HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)