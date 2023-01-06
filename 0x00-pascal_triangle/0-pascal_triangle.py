#!/usr/bin/python3
"""A program that implements Pascal Triangle"""


def pascal_triangle(n):
    """A function that returns a list of lists of numbers
    representing the pascal triangle"""
    pascal_list = [[1], [1, 1]]
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return pascal_list
    for i in range(3, n+1):
        previous_row = pascal_list[-1]
        previous_len = len(previous_row)
        temp = list(range(previous_len + 1))
        for x in range(previous_len):
            if x == 0:
                temp[x] = previous_row[x]
            else:
                temp[x] = previous_row[x] + previous_row[x-1]
        temp[-1] = 1
        previous_row = temp
        pascal_list.append(temp)
    return pascal_list
