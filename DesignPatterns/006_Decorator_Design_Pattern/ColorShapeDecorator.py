from ShapeDecorator import *

class ColorShapeDecorator(ShapeDecorator):
	def __init__(self,shape):
		super().__init__(shape)

	def draw(self):
		print("With Color")
		super().draw()