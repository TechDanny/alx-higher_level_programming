#!/usr/bin/python3
def add_integer(a, b=98):
    """
    this function adds two integers
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)

    return result
