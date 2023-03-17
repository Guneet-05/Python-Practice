from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()
# we call start in place of run
t1.start()
sleep(0.2) # to avoid colision
t2.start()

# if we have to print this at the end, we have to use join
t1.join()
t2.join()
print("Bye")