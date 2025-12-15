import numpy as np 

my_arr = np.random.randint(-5, 22, 12)

print(my_arr)

print("*****************************")

my_arr2 = my_arr.reshape(4, 3)

print(my_arr2)

# [21 13 -4 16 12 21  3  1 -5 11 11  6]
# *****************************
# [[21 13 -4]
#  [16 12 21]
#  [ 3  1 -5]
#  [11 11  6]]
