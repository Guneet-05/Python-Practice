n = int(input())
arr=[]

print("Enter a sorted array")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter a target value"))

lo,hi=0,len(arr)-1
flag = False

while lo<=hi:
    mid = lo + (hi-lo)//2
    if(arr[mid]==target):
        flag = True
        print("The value is found at index",mid)
        break
    elif(arr[mid]<target):
        lo=mid+1
    else:
        hi=mid-1

if not flag:
    print("The value does not exist in the array")