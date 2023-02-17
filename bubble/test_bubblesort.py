# test_bubblesort.py
"""Testing BubbleSort."""

from bubblesort import BubbleSort


def test_isSorted():
    """Testing isSorted."""
    bs = BubbleSort([1, 2, 3])
    assert bs.isSorted()


def test_next():
    """Testing next."""
    bs = BubbleSort([3, 2, 1])
    assert bs.next() == [2, 1, 3]
    assert bs.next() == [1, 2, 3]
