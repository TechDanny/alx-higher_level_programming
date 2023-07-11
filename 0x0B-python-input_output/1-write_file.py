#!/usr/bin/python3
"""
define a function
"""


def write_file(filename="", text=""):
    """
    add content in a file
    """
    with open(filename, "w", encoding="UTF8") as fw:
        fw.write(text)
        with open(filename, "r", encoding="UTF8") as f:
            return (len(text))
