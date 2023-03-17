from Singleton import *
import threading

# Here, you can call the constructor once for the 1st time
# After this, you will get the exception
# objUsingCons = Singleton()
# print(objUsingCons)

# These objects will be the same as that created by constructor if it is
# written before them. Else, the object will be created by the first call
# to getTheSingleInstance()

lock = threading.Lock()
obj = Singleton.getTheSingleInstance(lock)
print(obj)
obj2 = Singleton.getTheSingleInstance(lock)
print(obj2)
obj3 = Singleton.getTheSingleInstance(lock)
print(obj3)

# Early:
# in the Singleton class we initialize __inst = Singleton()
# This means that before even creating an object, an object already exists

# Lazy:
# it is what we have done i.e. kept __inst as None initially. Jab tak hum nahi kahenge
# object nahi banega
