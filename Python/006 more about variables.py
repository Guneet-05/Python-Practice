num = 5
print(num)

# the id method returns the address of the variable
print(id(num))

name = "Guneet"
print(name)
print(id(name))

a = 10
b = 20

print(a)
print(b)

print(id(a))
print(id(b))

# What happens on assignment operation

b = a

print(a)
print(b)

print(id(a)) # id of remains the same
print(id(b)) # id of b becomes the id of a

# variables (names of these variables like a, b) are also called as tags

# In python, we cannot make variables constant
# we can just make a person understand that we are trying to have a constant here
# by writing the variable name in uppercase letters

# this depicts PI is a constant
PI = 3.141

print(type(PI)) # will give class 'float'
