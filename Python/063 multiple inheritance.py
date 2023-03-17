class A:
    def meth(self):
        print("Class A method called")

class B (A):
    def meth(self):
        print("Class B method called")

class C (A):
    def meth(self):
        print("Class C method called")

class D (B,C):
    def meth2(self):
        print("Meth 2 is specific to class D")

d = D()
d.meth() # B will be printed
# if meth() is not in B, it will search in C, if not in C then A
d.meth2()