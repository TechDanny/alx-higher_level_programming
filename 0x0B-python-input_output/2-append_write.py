#!/usr/bin/python3
"""
define a function
"""


def append_write(filename="", text=""):
    """
    add content in a file
    """
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
        with open(filename, "r", encoding="UTF8") as fn:
            return (len(text))
