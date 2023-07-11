#!/usr/bin/python3
"""
define a function
"""


def read_file(filename=""):
    with open("my_file_0.txt", "r", encoding="UTF8") as f:
        for lines in f:
            print(lines, end="")
