from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from service.settings import DB_URL, RUN_TYPE


def set_engine():
    print(RUN_TYPE)
    return create_engine(DB_URL[RUN_TYPE])


engine = set_engine()
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
