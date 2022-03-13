from datetime import datetime
from typing import Optional

import service.errors
from service.db import db_session
from service.models import Measurements


class MeasurementsRepo:

    def add(
        self,
        name: str,
        status: str,
        description: str,
        measure_time: datetime,
        test_id: int,
    ) -> Measurements:
        measure: Measurements = Measurements(
            name=name,
            status=status,
            description=description,
            measure_time=measure_time,
            test_id=test_id,
        )
        db_session.add(measure)
        db_session.commit()
        return measure

    def update(
        self,
        uid: int,
        name: str,
        status: str,
        description: str,
        measure_time: datetime,
        test_id: int,
    ) -> Optional[Measurements]:
        measure: Measurements = Measurements.query.filter_by(uid=uid).first()
        if not measure:
            return None
        measure.name = name
        measure.status = status
        measure.description = description
        measure.measure_time = measure_time
        measure.test_id = test_id
        db_session.commit()
        return measure

    def get_all(self) -> Measurements:
        return Measurements.query.all()

    def get_by_uid(self, uid: int) -> Optional[Measurements]:
        measure: Measurements = Measurements.query.filter_by(uid=uid).first()
        if not measure:
            return None
        return measure

    def delete(self, uid: int) -> bool:
        measure = Measurements.query.filter_by(uid=uid).first()
        if not measure:
            return False
        db_session.delete(measure)
        db_session.commit()
        return True
