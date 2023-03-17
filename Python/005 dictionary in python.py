# the key should be of immutable type
data = {"Guneet":100,"Yash":200}
print(data)

# this will give the error unhashable type 'list'
# because list is a mutable type and the keys should be immutable
# values = [10,20,30]
# map = {values:10}

print(data["Guneet"])

# data[key] and if key does not exist, we get an error

print(data.get("Guneet"))
print(data.get(10)) # this does not give an error
# it returns none

# a dictionary can also have different data type keys at the same time
data[10] = "Ahan"
print(data)

print(data.get(100,"The key is not found"))

# creating a dictionary from lists
keys = ['Guneet', 'Ahan','Lavish']
values = ["Java","Python","C++"]

data = dict(zip(keys,values))
print(data)

# deleting a value
del data["Guneet"]
print(data)

# nested dictionary

progs = {'C++':'Codeblocks',
'Java':{'SE':'Netbeans','EE':'Eclipse'},
'Python':['VS Code','Sublime','Pycharm']}

print(progs)

print(progs['Java']['SE'])