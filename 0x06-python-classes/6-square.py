#!/usr/bin/python3
"""
class definition
"""
class Square:
    """
    instance attribute
    """
    def __init__(self, size=0, position(0, 0)):
        """
        private keys
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        retrieve
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter

