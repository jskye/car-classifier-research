# # define Point class
class Point(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def getXCoord(self):
        return self.x
    def getYCoord(self):
        return self.y
    def __str__(self):
     return "("+str(self.getXCoord()) + ', ' + \
        str(self.getYCoord()) +")"
