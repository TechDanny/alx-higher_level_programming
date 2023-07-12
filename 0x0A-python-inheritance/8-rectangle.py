#!/usr/bin/python3
"""
defines a class geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
defines a class Rectangle
that inherits from basegeometry
"""


class Rectangle(BaseGeometry):
    """
    create instances
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
