from sqlalchemy import Column, DateTime, Integer, String

from service.db import Base, engine


class Trials(Base):
    __tablename__ = 'trials'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    smd = Column(String)
    status = Column(String(5))
    value_description = Column(String)
    single_value = Column(String)
    trial_object = Column(String)
    measure_id = Column(Integer)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Trials name="{self.name}" status="{self.status}">'


class Measurement(Base):
    __tablename__ = 'measurements'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    measurement_object = Column(String)
    project = Column(String)
    report_date = Column(DateTime)
    responsible_person = Column(String)

    def __repr__(self):
        return f'<Measurements object="{self.measurement_object}" date="{self.date}">'


def create_schema():
    Base.metadata.create_all(bind=engine)
