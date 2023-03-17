class SolStereo:
    def __init__(self) -> None:
        self.__volume = 5
    
    def on(self):
        print("Turn on the stereo")
    
    def off(self):
        print("Turn off the stereo")
    
    def incVolume(self,delta):
        self.__volume += delta
        print("Volume set to",self.__volume)
    
    def decVolume(self,delta):
        self.__volume -= delta
        print("Volume set to",self.__volume)

