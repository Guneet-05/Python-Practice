# If there is a bird that is walking like a duck
# swimming like a suck and quaking like a duck
# then that bird is a duck
# This means that doesn't matter if it is a duck or not
# it behaves like a duck

class VSCode:

    def execute(self):
        print("VSCode compiles and executes the program")

class MyIDE:

    def execute(self):
        print("MyIDE compiles and executes the program")
        print("MyIDE provides syntax correction for python")
        print("MyIDE provides spell chekc for English Language")

class Laptop:

    def code(self,ide):
        ide.execute()
    

laptop = Laptop()
ide1 = VSCode()
ide2 = MyIDE()
# Since the code() method requires a class with method execute()
# Both the classes' objects can be passed
# as they both have execute() method, it does nto matter what the class is
laptop.code(ide1)
laptop.code(ide2)