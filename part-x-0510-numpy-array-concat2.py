import numpy as np 

x = np.array([[3, 4, 5]])

y = np.array([[13, 24, 35]])

# axis 0 row, axis 1 column

con_arr1 = np.concatenate([x, y], axis=1)

print(con_arr1)

con_arr2 = np.concatenate([x, y]) # default axis=0

print(con_arr2)

# [[ 3  4  5 13 24 35]]

# [[ 3  4  5]
#  [13 24 35]]
