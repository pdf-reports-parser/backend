from sqlalchemy import Column, Integer, String, TIMESTAMP
from service.db import Base, engine

class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String(5))
    description = Column(String)
    measure_time = Column(TIMESTAMP)
    test_id = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<Measurements name="{self.name}" status="{self.status}">'

def create_model():
    Base.metadata.create_all(bind=engine)
