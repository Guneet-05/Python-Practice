from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self,next) -> None:
        self._next = next
    
    @abstractmethod
    def handleRequest(self,req):
        pass