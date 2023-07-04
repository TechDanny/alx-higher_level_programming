#!/usr/bin/python3
"""
create rectangle class
"""


class Rectangle:
    """public class attribute"""
    number_of_instances = 0
    print_symbol = "#"
    """
    instances
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        set width value
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
        set height value
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
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height + self.__width + self.__height + self.__width

    def __str__(self):
        """
        prints rectangle with #
        """
        if self.height == 0 or self.width == 0:
            return ""
        str_rec = ""
        for i in range(self.height):
            str_rec = str_rec + str(Rectangle.print_symbol) * self.width + "\n"
        return str_rec.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangl...")
        Rectangle.number_of_instances -= 1
