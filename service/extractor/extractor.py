from dataclasses import asdict
from pathlib import Path

import aquaparser

from service import schemas
from service.repos.measurements import MeasurementsRepo
from service.repos.trials import TrialsRepo

measurement_repo = MeasurementsRepo()
trial_repo = TrialsRepo()


def write_to_bd_title(measurement_report):
    payload = asdict(measurement_report.title)
    payload['uid'] = -1
    measurement = schemas.Measurement(**payload)
    entity = measurement_repo.add(
        measurement_object=measurement.measurement_object,
        project=measurement.project,
        report_date=measurement.report_date,
        responsible_person=measurement.responsible_person,
    )
    new_measurement = schemas.Measurement.from_orm(entity)
    measure_id = new_measurement.uid
    return measure_id, new_measurement.dict()


def write_to_bd_trials(measurement_report, measure_id: int):
    trials_list = []
    for toc in measurement_report.toc:
        payload = asdict(toc)
        payload['uid'] = -1
        payload['measure_id'] = measure_id
        trial = schemas.Trial(**payload)
        entity = trial_repo.add(
            smd=trial.smd,
            status=trial.status,
            value_description=trial.value_description,
            single_value=trial.single_value,
            trial_object=trial.trial_object,
            measure_id=trial.measure_id,
        )

        new_trial = schemas.Trial.from_orm(entity)
        trials_list.append(new_trial.dict())
    return trials_list


def measurement_to_db(filename: Path):
    measurement = aquaparser.parse(filename.__str__())
    measure_id, title = write_to_bd_title(measurement)
    write_to_bd_trials(measurement, measure_id)
    return {'measurement': title}
