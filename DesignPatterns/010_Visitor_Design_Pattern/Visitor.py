from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitCircle(self,circle):
        pass

    @abstractmethod
    def visitRectangle(self,rectangle):
        pass

    @abstractmethod
    def visitTriangle(self,triangle):
        pass