# Abstract classes are not by default supported in Python
# We can however use them using the abc module 
# abc = abstract base classes

from abc import ABC, abstractmethod

class Computer (ABC):
    # This method that has definition and no body is an abstract method
    # and a class having abstract methods should be an abstract class
    @abstractmethod
    def process(self):
        pass

    def meth():
        print("This is a non abstract method")

class Laptop(Computer):
    def process(self):
        print("process of Computer overided in laptop")

# However, we should not be allowed to create objects of abstract classes
# com = Computer()
# com.process()

laptop = Laptop()
laptop.process()

# Now, we get an error that can't instantiate an abstract class

# same logic here as well i.e.
# when a class inherits an abstract class it becomes abstract until
# all the abstract methods are overriden in the child class
# Only abstract methods need to be overridden 

# So, if we have a class Class_Name(ABC) -> this is now an abstract class
# even if there are non-abstract methods in this class too
# However, an abstract class needs to have atleast one abstract method 
# Hence, we can say that an abstract class is a class with 
# one or more abstract methods