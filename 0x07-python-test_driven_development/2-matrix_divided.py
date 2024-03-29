#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError, ZeroDivisionError.
    Returns:
        A new matrix representing the result of the division.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    condition = (not isinstance(matrix, list))
    condition = condition or (matrix == [])
    condition = condition or (not all(isinstance(row, list) for row in matrix))
    if condition:
        raise TypeError(error)
    condition = not all((isinstance(ele, int) or isinstance(ele, float))
                        for ele in [num for row in matrix for num in row])
    if condition:
        raise TypeError(error)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
