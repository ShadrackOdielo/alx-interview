#!/usr/bin/env python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the given number of rows (n).

    Arguments:
        n (int): The number of rows for Pascal's Triangle.

    Returns:
        list of list of int: Pascal's Triangle as a list of lists.

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle
