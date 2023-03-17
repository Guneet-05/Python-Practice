from FlyNoWay import *
from Squeak import *
from MallardDuck import *

def main():
    mallard1 = MallardDuck()
    mallard1.performFly()
    mallard1.performQuack()

    mallard1.setFlyBehavior(FlyNoWay())
    mallard1.setQuackBehavior(Squeak())
    print("After changing the behaviors")
    mallard1.performFly()
    mallard1.performQuack()

if __name__ =='__main__':
    main()