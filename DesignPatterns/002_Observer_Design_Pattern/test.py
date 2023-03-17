from WeatherData import *
from CurrentConditionsDisplay import *

def main():
    weatherDataObject = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherDataObject)
    weatherDataObject.addObserver(currentDisplay)
    weatherDataObject.setMeasurements('8 C','45.56 Pressure','65%')

if __name__ == '__main__':
    main()