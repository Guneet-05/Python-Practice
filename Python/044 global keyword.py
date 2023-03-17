a = 10 # global variable
b = 12
c = 17
def fun():
    a = 8 # local variable -> preference will be given to local variable
    b = 15
    #So, if we don't want to create a local c and want to make changes
    # to the global c inside the function, we have to specify it a shown below.
    global c
    c = 20
    print("Local a",a)
    print("Local b",b)
    print("Global c",c)

    # However, now we won't be able to create aa local variable c in the function
    # because c = 100 will also be treated as a change to the global variable

fun()
print("Global a",a)
print("Global b",b)
print("Global c",c)

# How to have a local variable and make change to the global variable
# inside the function

k = 100

print('Global k before calling the function',k)

def meth():
    k = 20
    print("Local k",k)
    print("Global k",globals()['k'])
    globals()['k'] = 200
    print("Changed value of global k inside the function",globals()['k'])

meth()
print("Global k after the function call",k)

# Output order for k
# 100
# 20
# 100
# 200
# 200