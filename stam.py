import numpy as np

# Example original matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]).astype(float)
mask = np.array([[1,0,0],[1,0,0],[1,0,0]]).astype(bool)
mask2 = np.array([[0,1,0],[0,1,0],[0,1,0]]).astype(bool)

matrix[mask] = -np.inf

print(matrix)