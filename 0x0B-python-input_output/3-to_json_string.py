#!/usr/bin/python3
"""
define a function
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON rep of an object
    """
    return (json.dumps(my_obj))
