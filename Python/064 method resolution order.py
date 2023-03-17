# MRO stands for Method resolution order
# When a method or init method is called for any class
# and that class is inherting from multiple classes
# the method is first searched in the class itself
# if it is not found, then the preference is from left to right
# for instance if we have C(A,B), the method being called
# will be first searched in C, if not found then in A and 
# finally in B. It is both for a normal method and __init__ method

class A:
    def __init__(self) -> None:
        print("Class A init method")
    
    def meth(self):
        print("Class A meth")

class B(A):
    def __init__(self) -> None:
        print("Class B init")
    
    def meth(self):
        print("Class B meth")

class C(A):
    def __init__(self) -> None:
        print("Class C init")
    
    def meth(self):
        print("Class C meth")

class D(B,C):
    def __init__(self) -> None:
        print("Class D init")
    

dObj = D() # D init will be called
dObj.meth() # super().meth() will be called and super will be B as D(B,C)