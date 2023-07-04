#!/usr/bin/python3
"""
find next integer in the list
"""
def max_integer(list=[]):
    """
    returns the largest integer in the list
    """
    if len(list) == 0:
        return None
    rslt = list[0]
    n = 1
    while n < len(list):
        if list[i] > rslt:
            rslt = list[n]
        n = n + 1
    return rslt
