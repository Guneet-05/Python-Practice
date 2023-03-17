# function definition
def greet():
    print("Hello, welcome to functions in python")

# function call
greet()


def add(a,b):
    return a+b

print(add(4,5))

# returning multiple values

# multiplication and division

def mul_div(x,y):
    return x*y,x/y

mul,div = mul_div(10,5)
print(mul,div)