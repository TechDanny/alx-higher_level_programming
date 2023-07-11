#!/usr/bin/python3
"""
create a class
"""


class Student:
    """
    create instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dict representation
        """
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        else:
            return self.__dict__
