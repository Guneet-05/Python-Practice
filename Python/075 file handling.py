f = open('MyData','r')
print(f)
# print(f.read())

f1 = open('abc','w')
f1.write('something')
f1.write(' People')

f2 = open('abc','a') # append
f2.write("\nThere is a lot more to do")

for data in f:
    print(data)