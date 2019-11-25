# author: Timofey Khirianov
# license: GPLv3
"""Module to calculate some math functions

factorial(n) -- function to calculate the production of 1*2*...*n for
non-negative numbers.

"""

def factorial(n):
    """Function to calculate the production of 1*2*...*n.
    
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    >>> factorial(5)
    120

    """
    x = 1
    for i in range(1, n + 1):
        x = x + i
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()    
