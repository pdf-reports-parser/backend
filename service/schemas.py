from datetime import datetime

from pydantic import BaseModel, constr


class Trial(BaseModel):
    uid: int
    name: constr(min_length=1)  # type: ignore
    status: constr(min_length=1)  # type: ignore
    unit: constr()  # type: ignore
    value: constr()  # type: ignore
    subject: constr(min_length=1)  # type: ignore
    measure_id: int

    class Config:
        orm_mode = True


class Measurement(BaseModel):
    uid: int
    subject: constr(min_length=1)  # type: ignore
    project: constr(min_length=1)  # type: ignore
    date: datetime
    responsible: constr(min_length=1)  # type: ignore

    class Config:
        orm_mode = True
