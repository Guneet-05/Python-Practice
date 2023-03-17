x = 2
print(x + 3) # in place of x, its value 2 will take its place

# Another way of doing the above operation
y = 3
print(x+y)

# Since these are 'variables', their values can be changed
x = 10
print(x)
print(x+y)

# In python, we do not need to define the type of the variable
# So, it is dynamically typed programming language 
# However, python is strongly typed
# This is because variables have a fixed data type and  
# the data type matters during the operation  
# It is dynamically typed because the data type is only 
# identified during the run time

# This will give error as we have not defined the variable abc yet
# print(abc)

# In python, _ is used to take the value of the output of the prev operation

# >>> 10 + 20
# 30
# >>> _ + 100
# 130

name = "Guneet"
print(name + " Malhotra")

print(name[0])
print(name[-1])

# Accessing an invalid index character gives index out of range error in python
# print(name[10])

# Printing substrings
print(name[1:4]) # print from character 1 to character 3 i.e. [start,end)
print(name[1:]) # will print till the end i.e. length -1
print(name[:4]) # will print from start i.e. 0
print(name[-5:-1]) # this is also valid, still last is not included
print(name[1:100]) # now it does not give error, it ends at length -1 itself

# Strings are immutable in python

# name[0] = 'a'

# the length can be known by using the length function
print(len(name))