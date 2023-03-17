from numpy import *

arr1 = array([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9]
])

print(arr1)
# number of dimensions
print(arr1.ndim)

print(arr1.shape) # it is giving no of rows and cols
print(arr1.size) # it gives size

print(arr1.flatten()) # this returns a flattened array

arr2 = arr1.flatten().reshape(2,2,3)
print(arr2) # this will be a 3-d array