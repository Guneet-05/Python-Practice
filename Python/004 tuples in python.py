tup = (21,26,14,15)
print(tup[1])

# We cannot change the values in a tuple
# Tuples are immutable in Python

# tup[1] = 10 # we get the error saying tuple does not support item assignment
print(tup.count(21))

# iterations in tuple is faster than list
# when we make a list from variables it is almost
# the same speed as making a tuple from the variables
# or is slightly slower. However, if we make a tuple from literals
# it is almost 3 times faster tha making a list from literals
# this is because the tuples made from literals
# is recognized as a literal itself by Python

# a set is just like a mathematical set
# the values won't repeat
# also, a set does not store the values in the same order as you input
# this is because this is actually a hashset
s = {10,11,8,9,5,6,3,4,7,2,1212,2056,-1,8,9,5}
print(s)

# set does not support indexing
# this is because the values are unordered

# print(s[1]) # this will give error that set object is not subscriptable

s.add(10000)
print(s)