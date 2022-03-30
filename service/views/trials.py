from http import HTTPStatus
from typing import Any, Optional

from flask import Blueprint, abort, jsonify, request

from service import schemas
from service.repos.trials import TrialsRepo

trial_view = Blueprint('trial_view', __name__)

repo = TrialsRepo()


@trial_view.get('/')
def get_trials():
    entities = repo.get_all()
    trials = [schemas.Trial.from_orm(entity).dict() for entity in entities]
    return jsonify(trials), HTTPStatus.OK


@trial_view.get('/<uid>')
def get_by_id(uid: int):
    entity = repo.get_by_uid(uid)
    if not entity:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    trial = schemas.Trial.from_orm(entity)
    return trial.dict(), HTTPStatus.OK


@trial_view.post('/')
def add_trial():
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    payload['uid'] = -1

    trial = schemas.Trial(**payload)
    entity = repo.add(
        smd=trial.smd,
        status=trial.status,
        value_description=trial.value_description,
        single_value=trial.single_value,
        trial_object=trial.trial_object,
        measure_id=trial.measure_id,
    )

    new_trial = schemas.Trial.from_orm(entity)
    return new_trial.dict(), HTTPStatus.CREATED


@trial_view.put('/<uid>')
def update_trial(uid: int):
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    payload['uid'] = uid

    trial = schemas.Trial(**payload)
    entity = repo.update(
        uid=uid,
        smd=trial.smd,
        status=trial.status,
        value_description=trial.value_description,
        single_value=trial.single_value,
        trial_object=trial.trial_object,
        measure_id=trial.measure_id,

    )

    if not entity:
        return {'message': 'trial not found'}, HTTPStatus.NOT_FOUND

    fresh_trial = schemas.Trial.from_orm(entity)
    return fresh_trial.dict(), HTTPStatus.OK


@trial_view.delete('/<uid>')
def delete_trial(uid: int):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
