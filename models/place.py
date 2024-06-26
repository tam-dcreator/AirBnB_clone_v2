#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    reviews = relationship(Review, cascade="all, delete", backref='place')
    amenity_ids = []
    amenities = relationship(Amenity, secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Review instances
        with place_id equals to the current Place.id =>
        It will be the FileStorage relationship between Place and Review
        """
        from models import storage
        instances = []
        for obj in storage.all(Review).values():
            if obj.place_id == self.id:
                instances.append(obj)
        return instances

    @property
    def amenities(self):
        """
        returns the list of Amenity instances based on the
        attribute amenity_ids that contains all Amenity.id
        linked to the Place
        """
        from models import storage
        instances = []
        for obj in storage.all(Amenity).values():
            if obj.id in self.amenity_ids:
                instances.append(obj)
        return instances

    @amenities.setter
    def amenities(self, obj):
        """
        that handles append method for adding an Amenity.id to
        the attribute amenity_ids.
        This method should accept only Amenity object,
        otherwise, do nothing.
        """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
