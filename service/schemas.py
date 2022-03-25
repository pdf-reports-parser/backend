from datetime import datetime

from pydantic import BaseModel, constr


class Trial(BaseModel):
    uid: int
    name: constr(min_length=1)  # type: ignore
    status: constr(min_length=1)  # type: ignore
    description: constr(min_length=1)  # type: ignore
    trial_time: datetime
    test_id: int

    class Config:
        orm_mode = True
