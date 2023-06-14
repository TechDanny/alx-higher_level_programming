#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_2 = {}
    for key, value in a_dictionary.items():
        dictionary_2[key] = value * 2
    return dictionary_2
