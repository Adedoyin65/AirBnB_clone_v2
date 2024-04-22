#!/usr/bin/python3
"""A database script"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        self.__engine = create_engine(mysql+mysqldb://{}:{}@{}:3306/{}
                                      .format(getenv(HBNB_MYSQL_USER),
                                              getenv(HBNB_MYSQL_PWD),
                                              getenv(HBNB_MYSQL_HOST),
                                              getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        if getenv(HBNB_ENV) == test:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in the database"""
        models = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                models[obj.__class__.__name__ + . + obj.id] = obj
        else:
            for cls in Base.__subclasses__():
                for obj in self.__session.query(cls).all():
                    models[obj.__class__.__name__ + . + obj.id] = obj
        return models

    def new(self, obj):
        """Adds new object to database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()
