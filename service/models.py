from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from service.db import Base, engine


class Trials(Base):
    __tablename__ = 'trials'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String(5))
    unit = Column(String)
    value = Column(String)
    subject = Column(String)
    measure_id = Column(Integer, ForeignKey('measurements.uid'))

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Trials name="{self.name}" status="{self.status}">'


class Measurement(Base):
    __tablename__ = 'measurements'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String)
    project = Column(String)
    date = Column(DateTime)
    responsible = Column(String)

    def __repr__(self):
        return f'<Measurements object="{self.measurement_object}" date="{self.date}">'


def create_schema():
    Base.metadata.create_all(bind=engine)
