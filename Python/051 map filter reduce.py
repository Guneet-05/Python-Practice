from functools import reduce

def is_even(n):
    return n%2==0

nums=[1,2,3,4,5,6,7,8,9,10]
evens = list(filter(is_even,nums))
print(evens)

# doing this with lambda

odds = list(filter(lambda n:n%2!=0,nums))
print(odds)

# map
doubles = list(map(lambda n:2*n,evens))
print(doubles)

# reduce
sum = reduce(lambda a,b:a+b,doubles)
print(sum)