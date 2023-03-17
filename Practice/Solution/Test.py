from Circle import *
from Rectangle import *
from BorderShapeDecorator import *
from ColorFillShapeDecorator import *

cir = Circle()
circleWithBorder = BorderShapeDecorator(cir)
circleWithBorder.draw()

print("------------------------")

rect = Rectangle()
rectangleWithBorder = BorderShapeDecorator(rect)
rectangleWithBorderAndColor = ColorFillShapeDecorator(rectangleWithBorder)

rectangleWithBorderAndColor.draw()