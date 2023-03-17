from Shape import *
from Visitor import *

class Circle(Shape):
    def draw(self):
        print('Draw a circle')
    
    def accept(self, visitor):
        visitor.visitCircle(self)