#!/usr/bin/python3
"""
defines a function
"""


def inherits_from(obj, a_class):
    """
    returns true if the object is isntance
    else otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
