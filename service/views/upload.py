from http import HTTPStatus
from pathlib import Path

from flask import Blueprint, abort, request
from werkzeug.utils import secure_filename

from service.extractor import extractor

upload = Blueprint('upload', __name__)


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

    measurement = extractor.measurement_to_db(upload_file)
    return measurement, HTTPStatus.ACCEPTED
