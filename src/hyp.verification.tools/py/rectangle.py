class Rectangle(object):
	def __init__(self, x,y,w, h):
		self.left = x
		self.top = y
		self.width = w
		self.height = h
	def left(self):
		return self.left
	def top(self):
		return self.top
	def width(self):
		return self.width
	def height(self):
		return self.height
	def setWidth(self, w):
		self.width = w
	def setHeight(self):
		self.height = h
	def area(self):
		return self.getWidth() * self.getHeight()
	left = property(left)
