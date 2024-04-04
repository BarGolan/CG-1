import numpy as np

# Example original matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
rolled_matrix_col_left = np.roll(matrix, -1, axis=1) #𝐼(𝑖, 𝑗 + 1)
rolled_matrix_col_right = np.roll(matrix, 1, axis=1) # 𝐼(𝑖, 𝑗 − 1)
rolled_matrix_row_down = np.roll(matrix, 1, axis=0) #𝐼(𝑖 − 1, 𝑗)

rolled_matrix_col_left[:,-1]=0
rolled_matrix_col_right[:,0]=0
rolled_matrix_row_down[0,:]=0



print(rolled_matrix_col_left)
print(rolled_matrix_col_right)
print(rolled_matrix_row_down)


C_L = np.abs(rolled_matrix_col_left - rolled_matrix_col_right) + np.abs(rolled_matrix_row_down-rolled_matrix_col_right)
print(C_L)
#𝑐D(𝑖, 𝑗) = |𝐼(𝑖, 𝑗 + 1) − 𝐼(𝑖, 𝑗 − 1)| + |𝐼(𝑖 − 1, 𝑗) − 𝐼(𝑖, 𝑗 − 1)|


#𝑐R (𝑖, 𝑗) = |𝐼(𝑖, 𝑗 + 1) − 𝐼(𝑖, 𝑗 − 1)| + |𝐼(𝑖, 𝑗 + 1) − 𝐼(𝑖 − 1, 𝑗)|
C_R = np.abs(rolled_matrix_col_left - rolled_matrix_col_right) + np.abs(rolled_matrix_col_left-rolled_matrix_row_down)

#𝑐V(𝑖, 𝑗) = |𝐼(𝑖, 𝑗 + 1) − 𝐼(𝑖, 𝑗 − 1)|
C_V = np.abs(rolled_matrix_col_left - rolled_matrix_col_right)