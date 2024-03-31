from utils import *
import numpy as np

array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

array_1d = np.array([[[1], [2], [3]],
                     [[4], [5], [6]],
                     [[7], [8], [9]]])

# Array of column indices to delete from each row
indexes = [0, 1, 0]

new = np.ones((3, 2, 1))
for row, col in enumerate(indexes):
    # np.stack(new, np.delete(arr[row], col))
    new[row] = np.delete(array_1d[row], col, axis=0)

print(new)