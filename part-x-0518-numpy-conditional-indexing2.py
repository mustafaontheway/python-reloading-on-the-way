import numpy as np 

arr = np.random.randint(-12, 26, size=(6, 6))

print(arr)

print("------------------------------------------")

arr_logical_condition = (arr > 3) & (arr < 10)

print(arr_logical_condition)

print("------------------------------------------")

print(arr[arr_logical_condition])

"""
[[ 17  21  -5  12   7   0]
 [ 12   3   3  14   3  10]
 [ 20  14 -10   4   1  25]
 [  9  21  22   5   5   1]
 [ -1  22  20   7  20  14]
 [  1  16  -1   8  22  -3]]
------------------------------------------
[[False False False False  True False]
 [False False False False False False]
 [False False False  True False False]
 [ True False False  True  True False]
 [False False False  True False False]
 [False False False  True False False]]
------------------------------------------
[7 4 9 5 5 7 8]

"""
