from ShapeDecorator import *

class BorderShapeDecorator(ShapeDecorator):
	def __init__(self,shape):
		super().__init__(shape)

	def draw(self):
		print("With Border")
		super().draw()