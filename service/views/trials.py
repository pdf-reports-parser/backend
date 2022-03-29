from http import HTTPStatus
from typing import Any, Optional

from flask import Blueprint, abort, jsonify, request

from service import schemas
from service.repos.trials import TrialsRepo

trial = Blueprint('trial', __name__)

repo = TrialsRepo()


@trial.get('/')
def get_trials():
    entities = repo.get_all()
    trials = [schemas.Trial.from_orm(entity).dict() for entity in entities]
    return jsonify(trials), HTTPStatus.OK


@trial.get('/<uid>')
def get_by_id(uid: int):
    entity = repo.get_by_uid(uid)
    if not entity:
        return {'message': 'measurment not found'}, HTTPStatus.NOT_FOUND
    trial_entity = schemas.Trial.from_orm(entity)
    return trial_entity.dict(), HTTPStatus.OK


@trial.post('/')
def add_trial():
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    payload['uid'] = -1

    trial_entity = schemas.Trial(**payload)
    entity = repo.add(
        name=trial_entity.name,
        status=trial_entity.status,
        description=trial_entity.description,
        trial_time=trial_entity.trial_time,
        test_id=trial_entity.test_id,
    )

    new_trial = schemas.Trial.from_orm(entity)
    return new_trial.dict(), HTTPStatus.CREATED


@trial.put('/<uid>')
def update_trial(uid: int):
    payload: Optional[Any] = request.json
    if not payload:
        abort(HTTPStatus.BAD_REQUEST, 'Тело запроса не может быть пустым')

    payload['uid'] = uid

    trial_entity = schemas.Trial(**payload)
    entity = repo.update(
        uid=uid,
        name=trial_entity.name,
        status=trial_entity.status,
        description=trial_entity.description,
        trial_time=trial_entity.trial_time,
        test_id=trial_entity.test_id,
    )

    if not entity:
        return {'message': 'trial not found'}, HTTPStatus.NOT_FOUND

    fresh_trial = schemas.Trial.from_orm(entity)
    return fresh_trial.dict(), HTTPStatus.OK


@trial.delete('/<uid>')
def delete_trial(uid: int):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
