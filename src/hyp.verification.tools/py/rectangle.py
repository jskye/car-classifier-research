# # define rectangle class
from Point import Point

class Rectangle(object):
    def __init__(self, x,y,w,h):
        self.leftXCoord = x
        self.topYCoord = y
        self.width = w
        self.height = h
        self.rightXCoord = self.leftXCoord+self.width
        self.bottomYCoord = self.topYCoord+self.height
    def getLeftXCoord(self):
        return self.leftXCoord
    def getRightXCoord(self):
        return self.rightXCoord
    def getTopYCoord(self):
        return self.topYCoord
    def getBottomYCoord(self):
        return self.bottomYCoord
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def setWidth(self, w):
        self.width = w
    def setHeight(self, h):
        self.height = h
    def area(self):
        return self.getWidth() * self.getHeight()
    def getCenter(self):
        centerX = int(round(float(self.leftXCoord) + 0.5* float(self.width)))
        centerY = int(round(float(self.topYCoord) + 0.5* float(self.height)))
        center = Point(centerX, centerY)
        return center
    def __str__(self):
     return "("+str(self.getLeftXCoord()) + ', ' + \
        str(self.getTopYCoord()) + ', ' + \
        str(self.getWidth()) + ', ' + \
        str(self.getHeight()) +")"
