#!/usr/bin/python3
"""
script that add all arguments in list
"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file")\
        .load_from_json_file
    try:
        item_file = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item_file = []
    item_file.extend(sys.argv[1:])
    save_to_json_file(item_file, "add_item.json")
