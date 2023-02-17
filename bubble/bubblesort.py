# bubblesort.py
"""An implementation of a bubble-sort generator."""


class BubbleSort:
    """The BubbleSort Generator."""

    def __init__(self, initial):
        """Return an initialized generator."""
        self.current = initial

    def next(self):
        """Return the next step."""
        for i in range(len(self.current)-1):
            if self.current[i] > self.current[i+1]:
                tmp = self.current[i]
                self.current[i] = self.current[i+1]
                self.current[i+1] = tmp
        return self.current

    def isSorted(self):
        """Check, if list is sorted."""
        return self.current == sorted(self.current)
