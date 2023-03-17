from abc import ABC,abstractmethod

class ISomeWork(ABC):
    @abstractmethod
    def fun1(self,x):
        pass

    @abstractmethod
    def fun2(self,x,y):
        pass