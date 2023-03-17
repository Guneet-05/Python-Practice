from ISomeWork import *
from RealWork import *

class CacheProxyWork(ISomeWork):

    def __init__(self) -> None:
        self.realWork = RealWork()
        self.fmap = dict()

    def fun1(self, x):
        if self.fmap.get(x) != None:
            print("Taking it from cache")
            return self.fmap[x]
        else:
            res = self.realWork.fun1(x)
            self.fmap[x] = res
            return res 
    
    def fun2(self, x, y):
        self.realWork.fun2(x,y)