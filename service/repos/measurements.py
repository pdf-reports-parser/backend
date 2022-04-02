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
        measurement_object: str,
        project: str,
        report_date: datetime,
        responsible_person: str,
    ) -> Measurement:
        measurement: Measurement = Measurement.query.filter_by(uid=uid).first()
        if not measurement:
            raise NotFoundError('measurement')
        try:
            measurement.measurement_object = measurement_object
            measurement.project = project
            measurement.report_date = report_date
            measurement.responsible_person = responsible_person
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
