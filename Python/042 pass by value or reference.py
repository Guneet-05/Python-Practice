# Python is neither pass by value nor pass by reference

def update(x):
    print("Address of x",id(x))
    x = 8
    print("Address of x ater updation",id(x)) # so, now the address changes
    print("x",x)

a = 10
update(a)
print("Address of a",id(a))
print("a",a)

# So, when we pass an immutable object as a parameter to the function
# the argument variable also points to the same value (as discussed before)
# however, when any updates are made to the immutable value in the function,
# new memory will be assigned to the argument vaariable of the function

# What if a mutable parameter is used?

def update_list(lst):
    lst.append(10)
    print("printing inside the function",lst)

lst = [100,200,300,400]
update_list(lst)
print("printing outside the function",lst)

# So, changes persist in this case