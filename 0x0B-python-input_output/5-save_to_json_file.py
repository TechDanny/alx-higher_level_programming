#!/usr/bin/python3
"""
define a function
"""


import json
import locale


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    """
    with open(filename, "w", encoding=locale.getpreferredencoding()) as f:
        json.dump(my_obj, f)
