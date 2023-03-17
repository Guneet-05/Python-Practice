from array import *

n = int(input())
arr = array('i',[])

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    print(arr[i],end=" ")


