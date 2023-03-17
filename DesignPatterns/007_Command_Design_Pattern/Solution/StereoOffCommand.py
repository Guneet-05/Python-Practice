from SolStereo import *
from Command import *

class StereoOffCommand(Command):
    def __init__(self,stereo) -> None:
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()
    
    def undo(self):
        self.stereo.on()