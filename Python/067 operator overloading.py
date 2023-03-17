# when you use an operator, the methods are called behind the scenes
print(10 + 20)
# print(int.__add__(10,20)) This is what is called behind the scenes
# for the above operation

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinate(x,y)

    def showData(self):
        print("x =",self.x)
        print("y =",self.y)
    
    # to override the print() method
    def __str__(self):
        return '({},{})'.format(self.x,self.y)

c1 = Coordinate(10,20)
c2 = Coordinate(100,200)
c3 = c1 + c2
print(c3)