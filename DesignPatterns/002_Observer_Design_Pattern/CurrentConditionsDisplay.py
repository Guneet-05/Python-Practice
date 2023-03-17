from Observer import *
from Display import *
from WeatherData import *

class CurrentConditionsDisplay(Observer,Display):
    
    def __init__(self,weatherData) -> None:
        self.__temp = None
        self.__pressure = None
        self.__weatherData = weatherData
    
    def update(self):
        # pull instead of push
        self.__temp = self.__weatherData.getTemp()
        self.__pressure = self.__weatherData.getPressure()
        self.display()
    
    def display(self):
        print("Current Conditions Display")
        print("Temp =",self.__temp)
        print("Pressure =",self.__pressure)