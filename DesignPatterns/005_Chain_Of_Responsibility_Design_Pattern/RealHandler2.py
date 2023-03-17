from Handler import *
from Request import *

class RealHandler2(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)
    
    def handleRequest(self, req):
        if req.state == 0:
            print("Real Handler 2 handles the 0 request")
        else:
            print("Real Handler 2 passses the request to its next")
            self._next.handleRequest(req) 