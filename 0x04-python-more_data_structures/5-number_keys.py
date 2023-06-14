#!/usr/bin/python3
def number_keys(a_dictionary):
    total_keys = 0
    key = list(a_dictionary.keys())
    for n in key:
        total_keys += 1
    return total_keys
