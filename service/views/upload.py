from http import HTTPStatus
from pathlib import Path

import aquaparser
from dataclasses import asdict
from flask import Blueprint, abort, jsonify, request
from werkzeug.utils import secure_filename

from service import schemas
from service.repos.trials import TrialsRepo

upload = Blueprint('upload', __name__)

repo = TrialsRepo()


def db_insert(filename: Path):
    measurement = aquaparser.parse(filename)
    measurement_return = {
        'measurement': asdict(measurement.title),
    }
    # the stub is necessary until we get the id of the new measurement from the database
    measure_id = 1
    trials_list = []
    for toc in measurement.toc:
        payload = asdict(toc)
        payload['uid'] = -1
        payload['measure_id'] = measure_id
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
        trials_list.append(new_trial.dict())
    measurement_return['trials'] = trials_list
    return measurement_return


@upload.post('/')
def download_file():
    upload_dir = Path('service/tmp')
    upload_file = upload_dir / 'report.pdf'

    if 'file' not in request.files:
        abort(HTTPStatus.BAD_REQUEST, 'В теле запроса должен передоваться файл ("file")')
    file = request.files['file']
    if not file.filename:
        abort(HTTPStatus.BAD_REQUEST, 'В теле запроса должен передоваться файл ("file")')
    filename = secure_filename(file.filename)
    if Path(filename).suffix != '.pdf':
        abort(HTTPStatus.BAD_REQUEST, 'Неподдерживаемый формат файла - необходим PDF')

    file.save(upload_file)

    measurement = db_insert(upload_file)
    return measurement, HTTPStatus.ACCEPTED
