n = int(input())
if n== 0:
    print("0")
elif n==1:
    print("0 1")
else:
    a,b,c=0,1,0
    print(a,b,end=" ")
    for i in range(2,n+1):
        c = a+b
        print(c,end=" ")
        a=b
        b=c

