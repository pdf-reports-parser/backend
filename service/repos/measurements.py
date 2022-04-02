from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.db import db_session
from service.errors import ConflictError, NotFoundError
from service.models import Measurement


class MeasurementsRepo:

    def add(
        self,
        subject: str,
        project: str,
        date: datetime,
        responsible: str,
    ) -> Measurement:
        measurement = Measurement(
            subject=subject,
            project=project,
            date=date,
            responsible=responsible,
        )
        db_session.add(measurement)
        db_session.commit()
        return measurement

    def get_all(self) -> Measurement:
        return Measurement.query.all()

    def get_by_uid(self, uid: int) -> Measurement:
        measurement: Measurement = Measurement.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        return measurement

    def update(
        self,
        uid: int,
        subject: str,
        project: str,
        date: datetime,
        responsible: str,
    ) -> Measurement:
        measurement: Measurement = Measurement.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        try:
            measurement.subject = subject
            measurement.project = project
            measurement.date = date
            measurement.responsible = responsible
            db_session.commit()
        except IntegrityError:
            raise ConflictError('measurement')
        return measurement

    def delete(self, uid: int) -> None:
        measurement: Measurement = Measurement.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        db_session.delete(measurement)
        db_session.commit()
