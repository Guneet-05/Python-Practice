from Shape import *
from Visitor import *

class Rectangle(Shape):
    def draw(self):
        print('Draw a Rectangle')
    
    def accept(self, visitor):
        visitor.visitRectangle(self)