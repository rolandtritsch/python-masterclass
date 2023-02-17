# fib.py
"""Implementation of Fibunacci sequence."""

import sys


def fib(n):
    """Return the nth element of the fibunacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(sys.argv[1])
print(fib(n))
