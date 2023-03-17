from SolStereo import *
from Command import *

class StereoOnCommand(Command):
    def __init__(self,stereo) -> None:
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
    
    def undo(self):
        self.stereo.off()