from sqlalchemy.exc import IntegrityError

from service.db import db_session
from service.errors import ConflictError, NotFoundError
from service.models import Trials


class TrialsRepo:

    def add(
        self,
        name: str,
        status: str,
        unit: str,
        value: str,
        subject: str,
        measure_id: int,
    ) -> Trials:
        trial: Trials = Trials(
            name=name,
            status=status,
            unit=unit,
            value=value,
            subject=subject,
            measure_id=measure_id,
        )
        db_session.add(trial)
        db_session.commit()
        return trial

    def update(
        self,
        uid: int,
        name: str,
        status: str,
        unit: str,
        value: str,
        subject: str,
        measure_id: int,
    ) -> Trials:
        trial: Trials = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        try:
            trial.name = name
            trial.status = status
            trial.unit = unit
            trial.value = value
            trial.subject = subject
            trial.measure_id = measure_id
            db_session.commit()
        except IntegrityError:
            raise ConflictError('trial')
        return trial

    def get_all(self) -> Trials:
        return Trials.query.all()

    def get_by_uid(self, uid: int) -> Trials:
        trial: Trials = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        return trial

    def get_by_measure_id(self, measure_id: int) -> Trials:
        return Trials.query.filter(Trials.measure_id == measure_id).all()

    def delete(self, uid: int) -> None:
        trial = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        db_session.delete(trial)
        db_session.commit()
