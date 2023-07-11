#!/usr/bin/python3
"""
define a function
"""


def read_file(filename=""):
    """
    open and read content from a file
    """
    with open(filename, "r", encoding="UTF8") as f:
        for lines in f:
            print(lines, end="")
