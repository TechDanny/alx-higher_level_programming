#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    returns True if an object isinstance
    returns False if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
