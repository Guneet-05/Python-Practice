from Shape import *
from Visitor import *

class Triangle(Shape):
    def draw(self):
        print('Draw a Triangle')
    
    def accept(self, visitor):
        visitor.visitTriangle(self)