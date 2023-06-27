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
        private key
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        private key
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
         prints in stdout the square with the character #
         """
        if self.__size == 0:
            print()
            return
        for n in range(self.__size):
            print(''.join(['#' for m in range(self.__size)]))
