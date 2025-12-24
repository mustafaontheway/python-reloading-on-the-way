import numpy as np 

arr = np.random.randint(-12, 26, size=(6, 6))

print(arr)

print("------------------------------------------")

sub_arr_row_indexes = np.array([0, 2, 3])

sub_arr_column_indexes = np.array([1, 5])

sub_arr = arr[np.ix_(sub_arr_row_indexes, sub_arr_column_indexes)]

print(sub_arr)

"""
[[  6  15   8   6   8   4]
 [  2  -3  18   8   7  24]
 [  7 -10  13  10   9  18]
 [  2  -2  18  -4   7  -8]
 [ 11  13   7  24  21  20]
 [  9   4  -6  23  11  22]]
------------------------------------------
[[ 15   4]
 [-10  18]
 [ -2  -8]]

"""
