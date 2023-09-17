#!/usr/bin/python3
"""
contains the class definition of State
"""


import sys

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    defining the State class
    """

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(256), nullable=False)
