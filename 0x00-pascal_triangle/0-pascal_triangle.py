#!/usr/bin/python3
""" A program that Implements Pascals triangle"""


def factorial(n):
    """
    obtain the factorial of an integer n
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        return False
    if n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact


def combination(n, r):
    """
    Calculates the combinatorial coefficients of n and r
    """
    if not isinstance(n, int) and not isinstance(r, int):
        raise TypeError("n and r must be integers")
    return int(factorial(n)/(factorial(n-r)*factorial(r)))


def pascal_triangle(n):
    """
    Construct the pascal triangle of height n
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    arr = []
    if n <= 0:
        return [arr]

    for a in range(n):
        pascal_list = []
        for b in range(a+1):
            pascal_list.append(combination(a, b))
        arr.append(pascal_list)
    return arr
