# program to identify if a number is prime or not

n = int(input())

if n==1:
    print("Neither prime nor composite")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number") # else will execute if break has not executed
