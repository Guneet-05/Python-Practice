from abc import ABC, abstractmethod
from FlyBehavior import *
from QuackBehavior import *
from FlyWithWings import *
from Quack import *

class Duck(ABC):
    def __init__(self) -> None:
        self.__flyBehavior = FlyWithWings()
        self.__quackBehavior = Quack()  

    def swim(self):
        print("Swim")
    
    @abstractmethod
    def display(self):
        pass

    def setFlyBehavior(self,flyBehavior):
        self.__flyBehavior = flyBehavior
    
    def setQuackBehavior(self,quackBehavior):
        self.__quackBehavior = quackBehavior
    
    def performFly(self):
        self.__flyBehavior.fly()
    
    def performQuack(self):
        self.__quackBehavior.quack()