#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float

place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False)
        )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False)
        user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False)
        name = Column(
            String(128),
            nullable=False)
        description = Column(
            String(1024),
            nullable=True)
        number_rooms = Column(
            Integer,
            nullable=False,
            default=0)
        number_bathrooms = Column(
            Integer,
            nullable=False,
            default=0)
        max_guest = Column(
            Integer,
            nullable=False,
            default=0)
        price_by_night = Column(
            Integer,
            nullable=False,
            default=0)
        latitude = Column(
            Float, nullable=True)
        longitude = Column(
            Float, nullable=True)

        reviews = relationship(
            'Review',
            backref='place',
            cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            #  back_populates="place_amenities",
            viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter for reviews"""
            from models.__init__ import storage
            from models.amenity import Review
            revs = []
            all_revs = storage.all(Review)
            for rev in all_revs:
                if self.id == rev.id:
                    revs.append(rev)
            return revs

        @property
        def amenities(self):
            """getter for amenities"""
            from models.__init__ import storage
            from models.amenity import Amenity
            amn_list = []
            all_amn = storage.all(Amenity)
            for am in all_amn:
                if self.id == am.id:
                    amn_list.append(am)
            return amn_list

        @amenities.setter
        def amenities(self, obj):
            """setter for amenities"""
            from models.__init__ import storage
            from models.amenity import Amenity
            if (isinstance(obj, storage.all(Amenity))):
                self.amenity_ids.append(obj.id)
