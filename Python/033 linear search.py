n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

target = int(input())

for i in range(len(arr)):
    if arr[i]==target:
        print(target,"found at index",i)
        break
else:
    print("The target was not found")