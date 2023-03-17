from EditorMemento import *

# Originator
class Editor:
    def __init__(self) -> None:
        self.text = None
        self.cursorX = None
        self.cursorY = None
        self.fs = None
        self.ff = None

    def write(self):
        pass

    def delete():
        pass

    def getSnapshot(self):
        return EditorMemento(self.text,self.cursorX,self.cursorY,self.fs,self.ff)

    def restore(self,m):
        self.text = m.getText()
        self.cursorX = m.getCursorX()
        self.cursorY = m.getCursorY()
        self.fs = m.getFs()
        self.ff = m.getFf()   

    def print(self):
        print(self.text)
        print(self.cursorX)
        print(self.cursorY)
        print(self.fs)
        print(self.ff)
        print('--------------------------------------')