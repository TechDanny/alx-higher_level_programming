#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        for x in y:
            print("{:d}".format(x), end=" ")
        print()
