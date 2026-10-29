# 1. Create a NumPy array containing odd integers from 11 to 29. Display its number of dimensions and totalnumber of elements.

import numpy as np

arr = np.arange(11, 30, 2)

print("Array: ", arr)
print("Dimension: ", arr.ndim)
print("Total Number of element: ", arr.size)
