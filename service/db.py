from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from service import config

app_config = config.load_from_env()

engine = create_engine(app_config.db_url)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
