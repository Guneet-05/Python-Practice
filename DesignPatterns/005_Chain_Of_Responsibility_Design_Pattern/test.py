from RealHandler1 import *
from RealHandler2 import *
from RealHandler3 import *
from Request import *

handler1 = RealHandler1(None)
handler2 = RealHandler2(handler1)
handler3 = RealHandler3(handler2)

# Chain
# h3 -> h2 -> h1 -> None

req = Request(10)
handler3.handleRequest(req)

# 1:53:55