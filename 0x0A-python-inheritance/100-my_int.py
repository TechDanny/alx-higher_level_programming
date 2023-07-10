#!/usr/bin/python3
"""
define a class
"""


class MyInt(int):
    """
    def a function
    """
    def __eq__(self, value):
        """
        define instances
        """
        return super().__ne__(value)
    """
    define function
    """
    def __ne__(self, value):
        """
        define instances
        """
        return super().__eq__(value)
