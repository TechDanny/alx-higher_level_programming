#!/usr/bin/python3
"""
define a class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    create instance attribute
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
