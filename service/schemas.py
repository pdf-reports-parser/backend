from pydantic import BaseModel, constr


class Trial(BaseModel):
    uid: int
    smd: constr(min_length=1)  # type: ignore
    status: constr(min_length=1)  # type: ignore
    value_description: constr()  # type: ignore
    single_value: constr()  # type: ignore
    trial_object: constr(min_length=1)  # type: ignore
    measure_id: int

    class Config:
        orm_mode = True


class Measurement(BaseModel):
    uid: int
    name: constr(min_length=1)  # type: ignore
    data: constr(min_length=1)  # type: ignore

    class Config:
        orm_mode = True
