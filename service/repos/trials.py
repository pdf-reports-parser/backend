from datetime import datetime

from sqlalchemy.exc import IntegrityError

from service.db import db_session
from service.errors import ConflictError, NotFoundError
from service.models import Trials


class TrialsRepo:

    def add(
        self,
        name: str,
        status: str,
        description: str,
        trial_time: datetime,
        test_id: int,
    ) -> Trials:
        trial: Trials = Trials(
            name=name,
            status=status,
            description=description,
            trial_time=trial_time,
            test_id=test_id,
        )
        db_session.add(trial)
        db_session.commit()
        return trial

    def update(
        self,
        uid: int,
        name: str,
        status: str,
        description: str,
        trial_time: datetime,
        test_id: int,
    ) -> Trials:
        trial: Trials = Trials.query.filter_by(uid=uid).first()
        if not trial:
            raise NotFoundError('trial')
        try:
            trial.name = name
            trial.status = status
            trial.description = description
            trial.trial_time = trial_time
            trial.test_id = test_id
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
