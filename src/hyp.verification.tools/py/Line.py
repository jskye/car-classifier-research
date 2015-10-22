# # define Line class
import math
class Line(object):
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2
    def getP1(self):
        return self.p1
    def getP2(self):
        return self.p2
    def getDistance(self):
        euclidean_dist = math.sqrt((self.p1.getXCoord() - self.p2.getXCoord())**2 + \
        (self.p1.getYCoord() - self.p2.getYCoord())**2)
        return euclidean_dist
    def __str__(self):
     return "("+str(self.getP1()) + ', ' + \
        str(self.getP2()) + ', ' + \
        'distance: '+ self.getDistance()+")"
