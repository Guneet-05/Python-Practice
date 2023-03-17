# 1 array()
from numpy import *

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

# 2 linspace()

# the 3 params are start stop and parts and stop is included in linspace()
arr1 = linspace(0,15,16) # divides he range 0 to 15 in 16 parts
print(arr1)

# if we don;t specify the 3rd param, by default 50 parts will be done

arr2 = linspace(0,15)
print(arr2)

# 3 arange()

# this is same as range, the 3 params are start, stop and no of steps
# stop is not included and by default no of steps=1
arr3 = arange(0,16)
print(arr3)

# 4 logspace()

arr4 = logspace(1,40,5)
# start from 10**1 and goes to 10**40 and divides the range in 5 parts
print(arr4)

# 5 zeroes()

# an array of size 5 with all 0s
arr5 = zeros(5)
print(arr5)

# 6 ones()

# an array of size 5 with all 1s
arr6 = ones(5,int) # now we can get all the elements in int format
print(arr6)