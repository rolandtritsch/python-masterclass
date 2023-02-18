# test_util.py
"""Testing utility functions."""

import util


def test_randlist():
    """Testing randlist."""
    number = 20
    size = 10
    scale = 5
    assert len(util.randlist(number, size, scale)) == number
