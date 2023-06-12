#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_one = tuple_a + (0, 0)
    b_two = tuple_b + (0, 0)
    total = (a_one[0] + b_two[0], a_one[1] + b_two[1])
    return total
