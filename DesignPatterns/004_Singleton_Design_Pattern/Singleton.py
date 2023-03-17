import threading
class Singleton:
    
    __inst = None
    def __init__(self) -> None:
        '''Virtual Private Constructor'''
        if Singleton.__inst != None:
            raise Exception("This is a singleton class")
        else:
            Singleton.__inst = self
        

    @staticmethod  
    def getTheSingleInstance(lock):
        if Singleton.__inst == None:
            lock.acquire()
            Singleton.__inst = Singleton()
            lock.release()
        
        return Singleton.__inst
        