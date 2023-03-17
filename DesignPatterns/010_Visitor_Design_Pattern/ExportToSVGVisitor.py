from Visitor import *

class ExportToSVGVisitor(Visitor):

    def visitCircle(self, circle):
        print("Circle is exported to SVG")
    
    def visitRectangle(self, rectangle):
        print("Rectangle is exported to SVG")
    
    def visitTriangle(self, triangle):
        print("Triangle is exported to SVG")