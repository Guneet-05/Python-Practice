from Subject import *
from Observer import *

class WeatherData(Subject):

    def __init__(self) -> None:
        self.__observers = []
        self.__temp = None
        self.__pressure = None
        self.__humidity = None

    def getTemp(self):
        return self.__temp
    
    def getPressure(self):
        return self.__pressure
    
    def getHumdity(self):
        return self.__humidity
    
    def addObserver(self, observer):
        self.__observers.append(observer)
    
    def removeObserver(self, observer):
        self.__observers.remove(observer)
    
    def notifyObservers(self):
        for ob in self.__observers:
            ob.update()
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self,temp,pressure,humidity):
        self.__temp = temp
        self.__pressure = pressure
        self.__humidity = humidity

        self.measurementsChanged()
