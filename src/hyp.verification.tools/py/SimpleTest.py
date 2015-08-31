__author__ = 'juliusskye'

from Rectangle import Rectangle
from CompareRectangles import CompareRectangles
from PIL import Image
import os, sys
import glob
import cv2
from scipy import misc
import numpy as np
import os.path

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

    def test(self, r1, r2):
        print("Area(r1): "+str(r1.area()))
        print("Area(r2): "+str(r2.area()))
        compare_rects = CompareRectangles(r1,r2)
        if compare_rects.rect_intersection() is not None:
            print("overlapping/intersection area: "+str(compare_rects.area_intersection()))
        else:
            print("no intersection area")
        print("jaccard index: " +str(compare_rects.jaccard_index()))
        print("rectangles similar: "+str(compare_rects.similar_rectangles()))
        print("\n")

    def printImage(self,r1,r2):
        filepath = "/Users/juliusskye/COMP4120 Car Detection/car-classifier-research/src/hyp.verification.tools/py/test.png"
        if os.path.exists(filepath):
            image = cv2.imread(filepath)
        else:
            height = 250
            width = 250
            image = np.zeros((height,width,3), np.uint8)

        cv2.rectangle(image, (r1.getLeftXCoord(), r1.getTopYCoord()), (r1.getLeftXCoord()+r1.getWidth(), r1.getTopYCoord()+r1.getHeight()), (255, 255, 0), 1)
        cv2.rectangle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), (r2.getLeftXCoord()+r2.getWidth(), r2.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
        misc.imsave(filepath, image)



test_instance = SimpleTest(1,2)

print("---------------------------------")
print("---------------------------------")
print("Testing Compare Rectangles Class")
print("---------------------------------")
print("---------------------------------")

# print(test_instance.add())
# print("boundaries: "+ str(test_instance.bounds()) + \
#     "inverse bounds: " + str(test_instance.inverse_bounds()))

# print("---------------------------------")
# print("case: same rects")
# print("---------------------------------")
# r1 = Rectangle(0,5,5,5)
# r2 = Rectangle(0,5,5,5)
# test_instance.test(r1,r2)
#
#
# print("---------------------------------")
# print("case: no intersection")
# print("---------------------------------")
# r1 = Rectangle(0,5,5,5)
# r2 = Rectangle(0,100,5,5)
# test_instance.test(r1,r2)


print("---------------------------------")
print("case: fully contained rectangle")
print("---------------------------------")
# r1 should contain r2, should be jaccard similar.
r1 = Rectangle(0,0,50,50)
r2 = Rectangle(0,0,40,40)
test_instance.test(r1,r2)
test_instance.printImage(r1,r2)


print("---------------------------------")
print("case: x contained rectangle")
print("---------------------------------")
r1 = Rectangle(0,100,50,50)
r2 = Rectangle(20,100,20,100)
test_instance.test(r1,r2)
test_instance.printImage(r1,r2)

#
#
# print("---------------------------------")
# print("case: y contained rectangle")
# print("---------------------------------")
# # fuly contained
# # r1 should contain r2, should be jaccard similar.
# r1 = Rectangle(0,5,5,5)
# r2 = Rectangle(0,4,4,4)
# print("Area(r1): "+str(r1.area()))
# print("Area(r2): "+str(r2.area()))
# compare_rects = CompareRectangles(r1,r2)
# print("overlapping/intersection area: "+str(compare_rects.rect_intersection().area()))
# print("jaccard index: " +str(compare_rects.jaccard_index()))
# print("rectangles similar: "+str(compare_rects.similar_rectangles()))
# print("\n")








# print(test_instance.simple_contains())
