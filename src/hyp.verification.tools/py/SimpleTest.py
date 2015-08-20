__author__ = 'juliusskye'

from Rectangle import Rectangle
from CompareRectangles import CompareRectangles

class SimpleTest(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b

    def bounds(self):# global variables for boundary tests
        self.boundary_tests = [0,1,-1,1,0]
        return self.boundary_tests

    def inverse_bounds(self):#initialise inverse results as results
        self.inverse_boundary_tests = self.boundary_tests
        for index in range(len(self.inverse_boundary_tests)):
            if index != 0:
                self.inverse_boundary_tests[index] =-1*self.inverse_boundary_tests[index]
        return self.inverse_boundary_tests


    def simple_contains(self):
        boundary_tests = [1, 0, 0, 1]
        print("testing if r1 fully contains r2")

        fullyContains = True
        for boundary in boundary_tests:
            print(boundary)
            if boundary ==0 or boundary == 1:
                print("boundary 1 continue")
                continue
            else:
                print("boundary not 1 break")
                fullyContains = False
                break

        print("r1 fully contains r2:" + str(fullyContains))


test_instance = SimpleTest(1,2)
# print(test_instance.add())
# print("boundaries: "+ str(test_instance.bounds()) + "inverse bounds: " + str(test_instance.inverse_bounds()))

r1 = Rectangle(0,5,5,5)
r2 = Rectangle(0,4,4,4)
r3 = Rectangle(100,100,5,5)
print(r1).area()
print(r2).area()
# print(r3.getRightXCoord())
compare_rects = CompareRectangles(r1,r2)
print("overlapping/intersection area: "+str(compare_rects.rect_intersection().area()))
print("jaccard index: " +str(compare_rects.jaccard_index()))
print("rectangles similar: "+str(compare_rects.similar_rectangles()))




# print(test_instance.simple_contains())