from http import HTTPStatus
from pathlib import Path

import aquaparser
from flask import Blueprint, abort, jsonify, request
from werkzeug.utils import secure_filename

upload = Blueprint('upload', __name__)


def file_handler(filename: Path):
    measurement = aquaparser.parse(filename)
    return measurement.toc


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
    toc = file_handler(upload_file)
    return jsonify(toc), HTTPStatus.ACCEPTED
