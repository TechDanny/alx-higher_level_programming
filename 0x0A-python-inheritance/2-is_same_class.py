#!/usr/bin/python3
"""
define a class function
"""


def is_same_class(obj, a_class):
    """
    returns True if an object isinstance
    returns False if otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
