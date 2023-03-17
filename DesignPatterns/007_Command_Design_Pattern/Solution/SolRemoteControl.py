from SolLight import *
from Command import *

class SolRemoteControl:
    def __init__(self) -> None:
        self.b1Command = None
        self.b2Command = None
        self.b3Command = None
        self.b4Command = None

    def btn1Click(self):
        if self.b1Command == None:
            print("No functionality")
            return
        self.b1Command.execute()

    def btn2Click(self):
        if self.b2Command == None:
            print("No functionality")
            return
        self.b2Command.execute()

    def btn3Click(self):
        if self.b3Command == None:
            print("No functionality")
            return
        self.b3Command.execute()

    def btn4Click(self):
        if self.b4Command == None:
            print("No functionality")
            return
        self.b4Command.execute()