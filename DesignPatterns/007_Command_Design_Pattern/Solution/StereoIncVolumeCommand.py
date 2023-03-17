from SolStereo import *
from Command import *

class StereoIncVolumeCommand(Command):
    def __init__(self,stereo) -> None:
        self.stereo = stereo
    
    def execute(self):
        self.stereo.incVolume(1)
    
    def undo(self):
        self.stereo.incVolume(-1)