#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City',
            backref='state',
            cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """getter for cities related to state"""
            # from models.__init__ import storage
            # from models.city import City
            cit_list = []
            city_stor = models.storage.all(City)
            for c in city_stor:
                if self.id == c.state_id:
                    cit_list.append(c)
            return cit_list
