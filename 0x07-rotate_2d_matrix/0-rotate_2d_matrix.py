#!/usr/bin/python3
"""
Rotating a 2D Matrix
"""


def transpose_matrix(matrix, n):
    """
    Transposing a matrix
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """
    Reversing a matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """
    Rotating a matrix
    """
    n = len(matrix)
    transpose_matrix(matrix, n)
    reverse_matrix(matrix)
    return matrix
