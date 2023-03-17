from SolStereo import *
from Command import *

class StereoDecVolumeCommand(Command):
    def __init__(self,stereo) -> None:
        self.stereo = stereo
    
    def execute(self):
        self.stereo.decVolume(1)
    
    def undo(self):
        self.stereo.decVolume(-1)