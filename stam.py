import numpy as np

# Example original matrix
active_masks = ["a","b"]
masks = {"a":[[0.,1.,0.],[1.,0.,1.],[1.,0.,1.]],"b":[[0.,0.,0.],[0.,1.,0.],[0.,0.,0.]]}
for mask in masks:
    masks[mask] = np.array(masks[mask]).astype(bool)
    
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]).astype(float)

for mask in active_masks:
    matrix[masks[mask]] = -np.inf

print(masks["a"])
print(masks["b"])
print(matrix)