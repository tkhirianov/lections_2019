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
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large

    """
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()    
