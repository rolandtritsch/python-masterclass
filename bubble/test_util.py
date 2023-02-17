# test_util.py
"""Testing utility functions."""

import util


def test_randlist():
    """Testing randlist."""
    length = 10
    list = util.randlist(length, 30)
    assert len(list) == length
