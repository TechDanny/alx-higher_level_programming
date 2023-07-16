#!/usr/bin/python3
"""
create a class that inherits from base
"""


from models.base import Base


class Rectangle(Base):
    """
    create a class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        set width rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        set height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        set the x coordinate of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        set the y coordinate of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints the stdout of the Rectangle instance
        with the character '#'
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for n in range(len(args)):
                if n == 0:
                    if not isinstance(args[n], int):
                        raise TypeError("id must be an integer")
                    self.id = args[n]
                elif n == 1:
                    self.__width = args[n]
                elif n == 2:
                    self.__height = args[n]
                elif n == 3:
                    self.__x = args[n]
                elif n == 4:
                    self.__y = args[n]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "height":
                    self.__height = value
                elif key == "width":
                    self.__width = value
                elif key == "y":
                    self.__y = value
                elif key == "x":
                    self.__x = value
