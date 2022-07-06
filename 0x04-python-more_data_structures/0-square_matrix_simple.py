#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [[]]:
        return None
    cols = len(matrix[0])
    rows = len(matrix)
    new_matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
