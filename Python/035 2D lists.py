
# The wrong method

# arr = [[0]*4]*4
# print(arr)

# arr[0][0] = 1
# print(arr)

arr=[]
rows = int(input())
cols = int(input())

for i in range(rows):
    col = []
    for j in range(cols):
        col.append(int(input()))
    arr.append(col)


for i in range(rows):
    for j in range(cols):
        print(arr[i][j],end=" ")
    print()

