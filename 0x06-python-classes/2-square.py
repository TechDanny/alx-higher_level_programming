#!/usr/bin/python3
"""
class definition
"""


class Square:
    """
    instance attribute
    """
    def __init__(self, size=0):
        """
        private attribute
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
