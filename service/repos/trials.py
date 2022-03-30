from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.db import db_session
from service.errors import ConflictError, NotFoundError
from service.models import Trials


class TrialsRepo:

    def add(
        self,
        smd: str,
        status: str,
        value_description: str,
        single_value: str,
        trial_object: str,
        measure_id: int,
    ) -> Trials:
        trial: Trials = Trials(
            smd=smd,
            status=status,
            value_description=value_description,
            single_value=single_value,
            trial_object=trial_object,
            measure_id=measure_id,
        )
        db_session.add(trial)
        db_session.commit()
        return trial

    def update(
        self,
        uid: int,
        smd: str,
        status: str,
        value_description: str,
        single_value: str,
        trial_object: str,
        measure_id: int,
    ) -> Trials:
        trial: Trials = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        try:
            trial.smd = smd
            trial.status = status
            trial.value_description = value_description
            trial.single_value = single_value
            trial.trial_object = trial_object
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

    def delete(self, uid: int) -> None:
        trial = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        db_session.delete(trial)
        db_session.commit()
