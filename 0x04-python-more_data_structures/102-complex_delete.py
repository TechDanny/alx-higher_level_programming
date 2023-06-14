#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictionary_2 = list(a_dictionary.keys())
    for n in dictionary_2:
        if value == a_dictionary.get(n):
            del a_dictionary[n]
    return a_dictionary        
