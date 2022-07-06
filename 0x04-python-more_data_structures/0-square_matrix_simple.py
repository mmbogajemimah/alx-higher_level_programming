#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0] * rows for i in range(rows)]

    if matrix == [[]]:
        print()
    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
