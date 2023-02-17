# num.py
"""Numpy example."""

import numpy as np

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(matrix[0][0])
print(matrix[matrix.shape[0]-1][matrix.shape[1]-1])
