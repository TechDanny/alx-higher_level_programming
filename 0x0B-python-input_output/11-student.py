#!/usr/bin/python3
"""
create a class
"""


class Student:
    """
    instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dict representation
        """
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for x in attrs:
            try:
                my_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass
        return my_dict

    def reload_from_json(self, json):
        """
        replaces all the attributes of student instance
        """
        for m in json:
            try:
                setattr(self, m, json[m])
            except FileNotFoundError:
                pass
