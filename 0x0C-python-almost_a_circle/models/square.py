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
