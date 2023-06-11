#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        for x in y:
            if x != y[-1]:
                print("{:d}".format(x), end=' ')
            else:
                print("{:d}".format(x))
