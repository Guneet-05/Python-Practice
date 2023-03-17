# The default depth of recursion is 1000
import sys

print(sys.getrecursionlimit()) # this will give 1000

# increasing recursion limit
sys.setrecursionlimit = 2000

count=0

def greet():
    print(count,"hello")
    globals()['count'] +=1
    greet()

greet()