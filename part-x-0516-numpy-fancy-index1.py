import numpy as np 

arr = np.random.randint(-12, 26, 15)

print(arr)

print("------------------------------------------")

sub_arr_indexes = [2, 6, 11, 13]

sub_arr = arr[sub_arr_indexes]

print(sub_arr)

# [ 15  17  20  17 -11   4  -7 -11  25   5  -8 -10  22  22  -9]
# ------------------------------------------
# [ 20  -7 -10  22]
