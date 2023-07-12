#!/usr/bin/python3
"""
define a class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    create instance attributes
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        prints the area of a rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        returns the following description
        [Rectangle] <width>/<height>
        """
        triangle_str = "[" + str(self.__class__.__name__) + "]"
        triangle_str = triangle_str + str(self.__width) + "/" +\
            str(self.__height)
        return triangle_str
