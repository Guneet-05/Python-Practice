from Visitor import *

class DrawBoundaryVisitor(Visitor):

    def visitCircle(self, circle):
        print("Circle boundary drawn")
    
    def visitRectangle(self, rectangle):
        print("Rectangle boundary drawn")
    
    def visitTriangle(self, triangle):
        print("Triangle boundary drawn")