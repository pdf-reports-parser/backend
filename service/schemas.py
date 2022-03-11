from datetime import datetime

from pydantic import BaseModel, constr


class Measurement(BaseModel):
    name: constr(min_length=1)
    status: constr(min_length=1)
    description: constr(min_length=1)
    measure_time: datetime
    test_id: int

    class Config:
        orm_mode = True
