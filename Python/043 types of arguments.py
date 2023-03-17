# formal arguments
def sum(a,b):
    return a+b

# actual arguments
print(sum(5,6))

# There are 4 types of actual arguments
# 1. Position

# age = 18 if for default type

def lucky_draw(name,age=18):
    print(name,"Welcome!! to the lucky draw")
    if age%10==0 and name[0]=='G':
        print("You have won the lucky draw")
    else:
        print("Better luck next time")

# Here, the actual argumnets should be in order as name is assumed to
# be a string and age an int in the function while performing operations


lucky_draw('Guneet',20)

# 2. Keyword

# if you don't know the positions, you can use the keywords also
lucky_draw(age=20,name='Guneet')

# 3. Default

# Let us say that we wan't that the default age for this contest should be 18
# So, if a user does not pass his/her age, it is assumed to be 18 as shown below

# Here, we won't get the lucky draw as the ag is 18 by default
# However, if we pass a parameter, the default values get overridden
lucky_draw('Guneet')

# 4. Variable Length

# let us say we want to multiply the numbers
# we can have different no of params
# for that we use these type of arguments
# the argument is a tuple here and we have to deal it with that way

def add(*b):
    sum=0
    for ele in b:
        sum+=ele
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))

# 5 Keyworded Variable Length kwargs

def details(name,**data):
    print("Name",name)
    
    for i,j in data.items():
        print(i,j)


details('Guneet',age=22,mobile_number = 987330)