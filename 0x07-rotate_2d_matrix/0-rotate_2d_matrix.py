#!/usr/bin/python3
"""Defining a function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotates 2d matrix in-place"""
    temp = [[]]
    N = len(matrix)  # = 3

    # Transposing the matrix by converting the rows into columns
    for i in range(N):
        for j in range(i, N):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse the elements in the matrix
    for i, list in enumerate(matrix):
        matrix[i] = list[::-1]
