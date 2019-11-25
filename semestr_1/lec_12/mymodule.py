# author: Timofey Khirianov
# license: GPLv3
"""Module to calculate some math functions

factorial(n) -- function to calculate the production of 1*2*...*n for
non-negative numbers.

"""

def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

