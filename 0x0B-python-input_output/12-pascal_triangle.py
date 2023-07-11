#!/usr/bin/python3
"""
define a function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the pascal's of triangle n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for x in range(1, n):
        row = [1]
        prev = triangle[x - 1]

        for m in range(1, x):
            row.append(prev[m - 1] + prev[m])
        row.append(1)
        triangle.append(row)
    return triangle
