from calc import *

print("Name file says",__name__) # the output will be __main__

# however, there is a print statement in calc 
# and there __name__ will be calc hee as we hav imported that module

def main():
    print("This is the main function")

# If we want main() to execute only if it is the very first file 
# else if it is being imported, we don't want to call main

if __name__ == "__main__":
    main()