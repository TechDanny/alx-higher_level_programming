#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    returns True if an object isinstance
    returns False if otherwise
    """
    return type(obj) is a_class
