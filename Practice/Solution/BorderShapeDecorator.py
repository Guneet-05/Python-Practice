from Shape import *

class BorderShapeDecorator(Shape):
    
    def __init__(self,shape) -> None:
        self.shape = shape
    
    def draw(self):
        self.shape.draw()
        print("Apply border to the shape")