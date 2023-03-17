from EditorMemento import *

class CareTaker:
    def __init__(self) -> None:
        self.hist = []
    
    def save(self,editMem):
        self.hist.append(editMem)
    
    def undo(self):
        return self.hist.pop()