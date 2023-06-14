#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()
    for n in range(len(matrix)):
        matrix2[n] = list(map(lambda x:x**2, matrix[n]))
    return(matrix2)
