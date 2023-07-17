#!/usr/bin/python3
"""
create a class square that inherits
from rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define a class constructor
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        create a super class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
        set the size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        define size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if not isinstance(args[0], int) and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int) and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "y":
                    self.y = value
                elif key == "x":
                    self.x = value
