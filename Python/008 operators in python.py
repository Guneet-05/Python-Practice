# Arithmetic operators
x = 10
y = 20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x//y) #Integer or floor division
print(x**y) # Power Calculation

# Assignment Operators

x = y
print(x)
print(y)

x = x + 2
print(x)
# This can also be written as shown below

x += 2
print(x)

# The above can be done for all the arithmetic operations
x //= 10
print(x)

x **= 10
print(x)

# Single line assignment for multiple variables
val1,val2 = 5,6

print(val1,val2)

# Unary operator
# ++ or -- are not there in python

num = 10
print(num)
num = -num # negates itself 
print(num)

# Relational Operators -> These are boolean statements

print(10 < 5)
print(10 > 5)
print(5 <= 5)
print(5 >= 5)
print(10 == 5)
print(10 != 5)

# Logical operators

print(5<6 and 8>9,"Your condition is not satisfied")
print(5<6 or 8>9,"Your condition is satisfied") 

print(not True) # will print False
print(not False) # will print True