# Python has 3 access modifiers
# public -> any data member or member function is by default public
#protected -> adding single underscore before the variable name or method name
# makes it a protected variable/method.
# Protected means only child classes have the access
# private -> adding double underscore makes the variable/method private.
# private means no one has the access

class Demo:
    # public data member
    var1 = None
    # protected data member
    _var2 = None
    # private data member
    __var3 = None

    def __init__(self,var1,var2,var3) -> None:
        self.var1 = var1
        self._var2 = var2
        self.__var3 =var3 
    
    def public(self):
        print("public method can be accessed from anywhere")
        print(self.var1,",",self._var2,",",self.__var3)

    def _protected(self):
        print("Accessible inside the child classes")
    
    def __private(self):
        print("Accessible only inside this class")
        

def main():
    obj = Demo(10,20,30)
    print(obj.var1)
    print(obj._var2)
    #var3 gives an error-> no attribute __var3
    # print(obj.__var3)
    obj.public()
    obj._protected()
    # this will give error-> no attribute __private
    # obj.__private()

if __name__ == "__main__":
    main()
    