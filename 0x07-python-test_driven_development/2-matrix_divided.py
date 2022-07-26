#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    divides each element in a matrix by div
    """
    for row in matrix:
        for element in row:
            if type(element) != int and type(element != float):
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must \
            have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[0 for _ in range(len(matrix[0]))]
                  for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
