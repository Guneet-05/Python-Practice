from Circle import *
from Rectangle import *
from Triangle import *
from BorderShapeDecorator import *
from ColorShapeDecorator import *

circle = Circle()
# circle.draw()

circleWithBorder = BorderShapeDecorator(circle)
# circleWithBorder.draw()

circleWithBorderWithColor = ColorShapeDecorator(circleWithBorder)
circleWithBorderWithColor.draw()