from sqlalchemy import Column, DateTime, Integer, String

from service.db import Base, engine


class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String(5))
    description = Column(String)
    measure_time = Column(DateTime)
    test_id = Column(String)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Measurements name="{self.name}" status="{self.status}">'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
