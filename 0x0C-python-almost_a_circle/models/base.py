#!/usr/bin/python3
"""
create a class
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation
        of list dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list) or not all(type(n) == dict
           for n in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
