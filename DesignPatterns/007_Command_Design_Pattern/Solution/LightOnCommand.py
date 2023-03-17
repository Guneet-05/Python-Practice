from Command import *
from SolLight import *

class LightOnCommand(Command):
    def __init__(self,light) -> None:
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()