#!/usr/bin/python3
"""
create a class Student
"""


class Student:
    """
    crreate instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dict representation of a student
        """
        dict_student = self.__dict__
        return dict_student
