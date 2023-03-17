
# Numeric Data Type has the following types

#int
a = 10
print(a)
print(type(a))

#float
f = 10.98765
print(f)
print(type(f))

#complex
cn = 10 + 7j
print(cn)
print(type(cn))

#bool
val = True
print(val)
print(type(val))

# type conversion

x = 1.786
y = int(x)
print("The value of x is",x)
print("The value of y is",y)

p = 100
q = float(p)
print(p)
print(q)

c = complex(10,9)
print(c)

# A boolean statement
print(9<10)

t = int(True)
f = int(False)
print(t)
print(f)

# Sequence Data Type -> List, Tuple, Set, String and Range come under sequence

# we don't have char in python. We can just use string whereever 
# we want to use characters

print(range(10))

print(list(range(10))) # prints the list 0 o 9

# list of all even numbers till 100

print(list(range(2,101,2))) # the first param is the start
# second param is the end so, it is [start,end)
# 3rd is the differenec or jump size.

#Dictionary -> hashmap, we already know this. 