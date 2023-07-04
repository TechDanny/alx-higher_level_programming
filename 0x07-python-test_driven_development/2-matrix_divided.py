#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    divides all the elements of a matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size_of_row= len(matrix[0])
    if not all(len(row) == size_of_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    get_matrix = []
    for row in matrix:
        get_new_row = [round(elem / div, 2) for elem in row]
        get_matrix.append(get_new_row)
    return get_matrix
