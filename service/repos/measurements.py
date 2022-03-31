from sqlalchemy.exc import IntegrityError

from service.db import db_session
from service.errors import ConflictError, NotFoundError
from service.models import Measurements


class MeasurementsRepo:

    def add(self, name: str, data: str) -> Measurements:
        measurement: Measurements = Measurements(name=name, data=data)
        db_session.add(measurement)
        db_session.commit()
        return measurement

    def get_all(self) -> Measurements:
        return Measurements.query.all()

    def get_by_uid(self, uid: int) -> Measurements:
        measurement: Measurements = Measurements.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        return measurement

    def update(self, uid: int, name: str, data: str) -> Measurements:
        measurement: Measurements = Measurements.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        try:
            measurement.name = name
            measurement.data = data
            db_session.commit()
        except IntegrityError:
            raise ConflictError('measurement')
        return measurement

    def delete(self, uid: int) -> None:
        measurement: Measurements = Measurements.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        db_session.delete(measurement)
        db_session.commit()
