from pathlib import Path

import aquaparser
from aquaparser.schemas import MeasurementTitle, MeasurementTOC

from service import schemas
from service.repos.measurements import MeasurementsRepo
from service.repos.trials import TrialsRepo

measurement_repo = MeasurementsRepo()
trial_repo = TrialsRepo()


class Extractor:

    def extract(self, filename: Path) -> schemas.Measurement:
        report = aquaparser.parse(str(filename))
        measurement = self._save(report.title)
        self._save_trials(report.toc, measurement.uid)
        return measurement

    def _save(self, title: MeasurementTitle) -> schemas.Measurement:
        entity = measurement_repo.add(
            subject=title.measurement_object,
            project=title.project,
            date=title.report_date,
            responsible=title.responsible_person,
        )
        return schemas.Measurement.from_orm(entity)

    def _save_trials(self, tocs: list[MeasurementTOC], measure_id: int) -> list[schemas.Trial]:
        trials_list = []
        for toc in tocs:

            entity = trial_repo.add(
                name=toc.smd,
                status=str(toc.status),
                unit=str(toc.value_description),
                value=str(toc.single_value),
                subject=str(toc.trial_object),
                measure_id=measure_id,
            )

            new_trial = schemas.Trial.from_orm(entity)
            trials_list.append(new_trial)
        return trials_list
