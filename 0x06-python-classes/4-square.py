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
        self.__size = size
    def area(self):
        """
        gets the area of square
        """
        return self.__size * self.__size
    @property
    def size(self):
        """
        gets the private attribute
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        square size
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
