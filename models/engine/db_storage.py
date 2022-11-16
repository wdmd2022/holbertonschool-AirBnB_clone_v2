#!/usr/bin/python3
""" This module defines a class to manage database storage for airbnb clone """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'State': State, 'City': City}


class DBStorage:
    """ blank """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initalize DB Storage object
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, given_cls=None):
        """
        Query on current database session objects depending on class name
        """
        query_dict = {}
        if given_cls is not None:
            for obj in self.__session.query(given_cls).all():
                name_and_id = "{}.{}".format(type(obj).__name__, obj.id)
                query_dict.update({"{}".format(name_and_id): obj})

        else:
            for cls_name in classes:
                for obj in self.__session.query(cls_name).all():
                    name_and_id = "{}.{}".format(type(obj).__name__, obj.id)
                    query_dict.update({"{}".format(name_and_id): obj})
        return query_dict

    def reload(self):
        """
        Create all tables in database + self.__session attribute
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def new(self, obj):
        """ add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """remove dunder session private attribute"""
        self.__session.close()
