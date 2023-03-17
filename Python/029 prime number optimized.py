from math import sqrt

n = int(input())

if n==1:
    print("Neither prime nor composite")
else:
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime Number")
