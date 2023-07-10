#!/usr/bin/python3
"""
defines a class function
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if the object is an instance
    else otherwise
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
