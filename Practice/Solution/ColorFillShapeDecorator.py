from Shape import *

class ColorFillShapeDecorator(Shape):
    
    def __init__(self,shape) -> None:
        self.shape = shape
    
    def draw(self):
        self.shape.draw()
        print("Fill color into the shape")