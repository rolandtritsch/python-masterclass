# util.py
"""Utility functions."""

from random import randint


def randlist(n, size, scale):
    """Return a list of n numbers ((1 to size) * scale)."""
    list = []
    for i in range(n):
        list.append(randint(1, size) * scale)
    return list
