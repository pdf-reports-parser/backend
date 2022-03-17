from datetime import datetime

from pydantic import BaseModel, constr


class Measurement(BaseModel):
    uid: int
    name: constr(min_length=1)  # type: ignore
    status: constr(min_length=1)  # type: ignore
    description: constr(min_length=1)  # type: ignore
    measure_time: datetime
    test_id: int

    class Config:
        orm_mode = True
