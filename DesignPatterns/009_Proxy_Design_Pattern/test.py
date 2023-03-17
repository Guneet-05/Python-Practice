# We will have a Real Class that has many functions
# There will be a proxy class that will have all the functions same as the real class
# Proxy can add its own smartness

# For instance -> Chaching Proxy 
# Generally proxy class tabhi lagti hai jab aapne apna design extensible banay ho
# accha design banaya ho

# Usually used in caching, protection (like authentication), add some extra smartness

# Used in remote processing in earlier days
# aaj jise api kehte hai use pehle webservices kehte the
# maan lo server pe web services hosted hai. Usme ek student class hai
# student class k getstudents method ko call karke ek students ki list milti hai
# server use apne aap json me convert karke client ko bhejta hai
# 
# lekin .net me apne aap url of the server add karne pe studentproxy class ban jaati thi
# ye actual class se method ko call karvati thi. Vaha se data json me aata tha to student
# proxy class apna ye proxy lagati thi ki vo use list me convert kar deti thi.

from RealWork import *
from CacheProxyWork import *

worker = CacheProxyWork()
print(worker.fun1(10))

print(worker.fun1(10))

