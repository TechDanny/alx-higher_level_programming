#!/usr/bin/python3
"""
create a rectangle class
"""


class Rectangle:
    """
    create instance attribute
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        sets the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        sets the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__width + self.__height + self.__width + self.__height

    def __str__(self):
        """
        prints rectangle with character #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        str_rec = ""
        for i in range(self.__height):
            str_rec = str_rec + "#" * self.__width + "\n"
        return str_rec
