#!/usr/bin/python3
"""
define a function
"""


def add_attribute(obj, name_of_attr, value_of_attr):
    """
    returns the total of all attributes
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name_of_attr, value_of_attr)
