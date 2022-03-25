from sqlalchemy import Column, DateTime, Integer, String

from service.db import Base, engine


class Trials(Base):
    __tablename__ = 'trials'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String(5))
    description = Column(String)
    trial_time = Column(DateTime)
    test_id = Column(String)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Trials name="{self.name}" status="{self.status}">'


def create_schema():
    Base.metadata.create_all(bind=engine)
