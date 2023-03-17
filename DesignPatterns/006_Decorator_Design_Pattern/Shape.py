from abc import ABC, abstractmethod

# Interface Shape
class Shape(ABC):
	@abstractmethod
	def draw(self):
		pass

