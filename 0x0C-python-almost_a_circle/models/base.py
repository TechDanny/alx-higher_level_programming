#!/usr/bin/python3
"""
create a class
"""


class Base:
    """
    define a private class attribute
    """
    __nb_objects = 0

    """
    define a class constructor
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
