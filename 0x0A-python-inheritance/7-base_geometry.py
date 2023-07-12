#!/usr/bin/python3
"""
create a basegeometry class
"""



class BaseGeometry:
    """
    define area function
    """
    def area(self):
        """
        return exception error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if the value is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
