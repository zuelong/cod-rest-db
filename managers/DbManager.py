from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DbManager:

    __engine = None
    Base.metadata.bind = __engine

    def __init__(self):
        self.DBSession = sessionmaker(bind=self.__engine)

    def create_db(self):
        Base.metadata.create_all(self.__engine)

    def get_session(self):
        return self.DBSession()

    @staticmethod
    def set_engine(path):
        DbManager.__engine = create_engine(path)
