from Light import *

class RemoteControl:
    def __init__(self) -> None:
        self.light = Light()

    def btn1Click(self):
        self.light.on()

    def btn2Click(self):
        self.light.off()

    def btn3Click(self):
        print("No functionality")

    def btn4Click(self):
        print("No functionality") 
    
# Remote control is tightly bound with the light
# Invoker (Remote) is tightly coupled with receiver (light)