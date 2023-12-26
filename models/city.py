#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from models.place import Place
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
