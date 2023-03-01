import matplotlib.pyplot as plt
import random

def quicksort(arr, left, right):
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
        plt.bar(range(len(arr)), arr)
        plt.show(block=False)
        plt.pause(0.1)
    quicksort(arr, left, j)
    quicksort(arr, i, right)

# Example usage
arr = [3, 7, 1, 2, 8, 4, 5]
quicksort(arr, 0, len(arr) - 1)
print(arr)
