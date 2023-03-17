from abc import ABC, abstractmethod

# Interface Subject
class Subject(ABC):

    @abstractmethod
    def addObserver(self,observer):
        pass

    @abstractmethod
    def removeObserver(self,observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass