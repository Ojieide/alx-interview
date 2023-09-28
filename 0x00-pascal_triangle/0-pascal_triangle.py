#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    else:
        res = []
        for i in range(n):
            if len(res) == 0:
                res.append([1])
            else:
                row = [1]
                for j in range(1, len(res[-1])):
                    row.append(res[-1][j] + res[-1][j - 1])
                row.append(1)
                res.append(row)
        return res
