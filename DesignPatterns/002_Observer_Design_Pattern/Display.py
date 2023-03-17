from abc import ABC, abstractmethod

# Interface display
class Display(ABC):
    @abstractmethod
    def display(self):
        pass