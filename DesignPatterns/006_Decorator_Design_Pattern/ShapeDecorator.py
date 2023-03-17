from Shape import *

class ShapeDecorator(Shape):

	def __init__(self,shape):
		self.__shape = shape

	# Overriding the draw method as it implements the shape interface
	
	def draw(self):
		self.__shape.draw()