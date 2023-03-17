from numpy import *

arr = array([1,2,3,4,5])

print(arr)

# add 5 to every element

for i in range(len(arr)):
    arr[i] += 5

print(arr)

# shortcut to do it

arr = arr + 5
print(arr)

# add elments of 2 arrays

arr1 = array([1,2,3,4,5])
arr2 = array([5,4,3,2,1])

for i in range(len(arr1)):
    arr1[i] = arr1[i]+arr2[i]

print(arr1)

# shortcut to do vectorized operation

a1 = array([1,2,3,4,5])
a2 = array([9,8,6,3,4])

a3 = a1 + a2
print(a3)

# some mathematical operations

print(sin(arr))
print(cos(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

# How to copy an array

# Shallow Copy (Aliasing)
arr1 = array([2,4,6,8])
arr2 = arr1

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

arr3 = arr1.view()
print(arr1)
print(arr2)
print(arr3)

print(id(arr1))
print(id(arr2))
print(id(arr3))

# Although views has created arr3 in different memory location, 
# it is still linked to arr1

arr1[1] = 10
print(arr1)
print(arr2)
print(arr3) # Still this is not a deep copy

# Deep copy

print("DEEP COPY")

arr4 = arr1.copy() # This will create a deep copy
arr1[2] = 20
print(arr1)
print(arr2)
print(arr3)
print(arr4)

print(id(arr1))
print(id(arr2))
print(id(arr3))
print(id(arr4))