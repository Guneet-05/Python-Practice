from SolRemoteControl import *
from SolLight import *
from SolStereo import *
from LightOnCommand import *
from LightOffCommand import *
from StereoOnCommand import *
from StereoOffCommand import *
from StereoIncVolumeCommand import *
from StereoDecVolumeCommand import *

rc = SolRemoteControl()
light = SolLight()
stereo = SolStereo()

rc.b1Command = LightOnCommand(light)
rc.b2Command = LightOffCommand(light)
rc.b3Command = StereoOnCommand(stereo)
rc.b4Command = StereoOffCommand(stereo)

rc.btn1Click()
rc.btn2Click()
rc.btn3Click()
rc.btn4Click()

# New setup
print("After new setup")
rc.b1Command = StereoIncVolumeCommand(stereo)
rc.b2Command = StereoDecVolumeCommand(stereo)

rc.btn4Click()
rc.btn3Click()
rc.btn2Click()
rc.btn1Click()