#!/usr/bin/python3
"""
create a function
"""


import json
import locale


def load_from_json_file(filename):
    """
    creates object from JSON file
    """
    with open(filename, "r", encoding=locale.getpreferredencoding()) as f:
        my_file = json.load(f)
        return my_file
