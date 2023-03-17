def topten():
    yield 1 # yield is similar to return, only now it returns a generator
    yield 2
    yield 3
    yield 4
    yield 5

values = topten()

print(values)

for i in values:
    print(i)