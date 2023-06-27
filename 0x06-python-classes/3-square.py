#!/usr/bin/python3
"""
classs definition
"""


class Square:
    """
    instance attribute
    """
    def __init__(self, size=0):
        """
        private attributes
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        """
        calculates area of square
        """
    def area(self):
        return self.__size * self.__size
