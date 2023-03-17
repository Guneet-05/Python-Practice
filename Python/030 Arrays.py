# In arrays, we have a collection of only one datatype at a time
# This means that if we are creating an int array, it will be int array only
# If we are creating a float array, it is a float array only.
# However, arrays in python are dynamic

from array import*

vals = array('i',[9,8,6,3,4,7,2])
print(vals)
print(vals.buffer_info()) # gives a tuple of 2 elements, address and size

# Reverese method does not return a values, it just revereses tha actual array

vals.reverse()
print(vals)

for i in vals:
    print(i)

# A character array

chars = array('u',['a','e','i','o','u'])
print(chars)

# copying values into a new array
newArray= array(vals.typecode,(a for a in vals))
newArray2 = array(vals.typecode,(a*a for a in vals))
print(newArray)
print(newArray2)

# printing an array using while loop

i = 0
while i<len(vals):
    print(vals[i])
    i+=1
