#!/usr/bin/python3
"""
contains class definition of city
"""


import sys
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    defining the City class
    """

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(256), nullable=False)
    states_unique = Column(Integer, ForeignKey("states.id"), nullable=False)
