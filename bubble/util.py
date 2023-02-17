# util.py
"""Utility functions."""

from constants import Constants
from random import randint


def randlist(n, upper):
    """Return a list of n numbers ((1 to upper) * scale)."""
    list = []
    for i in range(n):
        list.append(randint(1, upper) * Constants.scale)
    return list
