a = 10
b = 20

print("Before swapping the values are")
print("a =",a,"b =",b)

# swapping with 3rd variable
temp = a
a = b
b = temp

print("After swapping the values are")
print("a =",a,"b =",b)

# swapping without third variable

a = a + b
b = a - b
a = a - b

print("After swapping the values 2 times the values are")
print("a =",a,"b =",b)

#XOR can also be used in place of + and -

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping the values 3 times the values are")
print("a =",a,"b =",b)

# another special way to swap 2 numbers in python
a,b = b,a

print("After swapping the values 4 times the values are")
print("a =",a,"b =",b)
