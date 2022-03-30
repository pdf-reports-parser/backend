from dataclasses import asdict
from pathlib import Path

import aquaparser

from service import schemas
from service.repos.trials import TrialsRepo

repo = TrialsRepo()


def write_to_bd_title(measurement):
    title = {
        'measurement': asdict(measurement.title),
    }
    # the stub is necessary until we get the id of the new measurement from the database
    measure_id = 1
    return measure_id, title


def write_to_bd_trials(measurement, measure_id: int):
    trials_list = []
    for toc in measurement.toc:
        payload = asdict(toc)
        payload['uid'] = -1
        payload['measure_id'] = measure_id
        trial = schemas.Trial(**payload)
        entity = repo.add(
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
    measurement = aquaparser.parse(filename)
    measure_id, title = write_to_bd_title(measurement)
    trials = write_to_bd_trials(measurement, measure_id)
    new_measurement = {
        'measurement': title,
        'trials': trials,
    }
    return new_measurement
