from Command import *
from SolLight import *

class LightOffCommand(Command):
    def __init__(self,light) -> None:
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()