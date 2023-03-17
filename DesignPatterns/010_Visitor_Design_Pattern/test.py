from Shape import *
from Circle import *
from Triangle import *
from Rectangle import *
from ExportToSVGVisitor import *
from DrawBoundaryVisitor import *

shapes = [Circle(),Rectangle(),Triangle()]
svgExportVis = ExportToSVGVisitor()
drawBoundaryVis = DrawBoundaryVisitor()

for shape in shapes:
    shape.draw()
    shape.accept(drawBoundaryVis)
    shape.accept(svgExportVis)

# New functionality is being added without changing or extending code of circle
#  rectangle and triangle 