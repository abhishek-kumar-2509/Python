# 3. Create a 4 x 3 NumPy array filled with 9. Change the element in the third row and second column to 0.


import numpy as np

arr = np.full((4, 3), 9)

arr[2, 1] = 0
print(arr)