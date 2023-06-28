#!/usr/bin/python3
"""
class definition
"""


import match


class MagicClass:
    """
    instance attribute
    """
    def __init__(self, radius=0):
        """
        private key
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        calculates the area
        """
        return self.__radius * self.__radius * math.pi

    def circumference(self):
        """
        calculates the circumference
        """
        return 2 * math.pi * self.__radius
