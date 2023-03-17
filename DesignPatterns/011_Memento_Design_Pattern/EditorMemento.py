from datetime import datetime

class EditorMemento:
    def __init__(self,text,cursorX,cursorY,fs,ff) -> None:
        self.__text = text
        self.__cursorX = cursorX
        self.__cursorY = cursorY
        self.__fs = fs
        self.__ff = ff
        moment = datetime.now()
    
    def getText(self):
        return self.__text
    
    def getCursorX(self):
        return self.__cursorX
    
    def getCursorY(self):
        return self.__cursorY

    def getFs(self):
        return self.__fs
    
    def getFf(self):
        return self.__ff