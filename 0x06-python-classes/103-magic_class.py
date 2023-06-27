#!/usr/bin/python3
"""
class definition
"""


import match


class MagicClass:
    """
    instance attribute
    """
    def __init__(self, rad=0):
        """
        private key
        """
        self.__rad = 0
        if isinstance(rad, int) and isinstance(rad, float):
            raise TypeError("radius must be a number")
        self.__rad = rad

    def area(self):
        """
        calculates the area
        """
        return self.__rad * self.__rad * math.pi

    def circum(self):
        """
        calculates the circumference
        """
        return 2 * math.pi * self.__rad
