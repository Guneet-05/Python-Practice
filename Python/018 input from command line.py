from sys import argv

# index 0 in argv is the file name
# index 1 is 1st command line argument, index 2 is second and so on

x = int(argv[1])
y = int(argv[2])
print("The result of addition from command line is",x+y)