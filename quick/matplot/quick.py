# quick.py
"""
A quick-sort visualizer (using matplot).

This code was generate by ChatGPT and then
(just) polished/refactored by me.
"""

import matplotlib.pyplot as plt
import random
import util


def quicksort(arr, left, right):
    """Sort the array and display the sorting."""
    if left >= right:
        return
    pivot = arr[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        plt.clf()
        plt.bar(range(len(arr)), arr)
        plt.show(block=False)
        plt.pause(0.2)
    quicksort(arr, left, j)
    quicksort(arr, i, right)

# Example usage
arr = util.randlist(100, 100, 1)
quicksort(arr, 0, len(arr) - 1)
print(arr)
