#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter method to return the list of City objects """
            from models import storage
            from models.city import City
            cities_list = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        a = "all, delete-orphan"
        cities = relationship("City", backref="state", cascade=a)
