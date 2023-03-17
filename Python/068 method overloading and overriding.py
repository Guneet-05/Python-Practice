# Method overloading is not there in python
# This means that in python, we cannot create 2 methods with the same name
class A:
    def meth(self):
        print("inside A meth()")

class B (A):
    # this method overrides the meth() of class A
    def meth(self):
        print("inside B meth()")

a = A()
a.meth()
b = B()
b.meth()