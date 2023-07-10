#!/usr/bin/python3
"""
create a child class
"""


class MyList(list):
    """
    prints a list in ascending order
    """
    def print_sorted(self):
        my_sort_list = sorted(self)
        print(my_sort_list)
