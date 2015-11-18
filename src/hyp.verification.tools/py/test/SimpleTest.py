__author__ = 'juliusskye'

import os, sys
sys.path.append('..')
from py.Rectangle import Rectangle
from py.CompareRectangles import CompareRectangles
from PIL import Image
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

        print("Rectangle r1: ["+str(r1.getLeftXCoord())+", "+str(r1.getTopYCoord())+", "+ \
        str(r1.getWidth())+", " + str(r1.getHeight())+"]"+" | Area(r1): "+str(r1.area()))
        print("Rectangle r2: ["+str(r2.getLeftXCoord())+", "+str(r2.getTopYCoord())+", "+ \
        str(r2.getWidth())+", " + str(r2.getHeight())+"]"+" | Area(r2): "+str(r2.area()))
        compare_rects = CompareRectangles(r1,r2, 0.35)
        # if compare_rects.rect_intersection() is not None:
        #     print("overlapping/intersection area: "+str(compare_rects.area_intersection()))
        #     print("union area: "+str(compare_rects.area_union()))
        # else:
        #     print("no intersection area")
        print(compare_rects.boundary_tests)
        print("union: " +str(compare_rects.area_union()))
        print("intersection: " +str(compare_rects.area_intersection()))
        # print("division result: "+ str(compare_rects.area_intersection() / compare_rects.area_union()))
        print("jaccard index: " +str(compare_rects.jaccard_index()))
        print("rectangles similar: "+str(compare_rects.similar_rectangles()))
        print("\n")

    def printImage(self,r1,r2):
        filepath = "/Users/juliusskye/COMP4120.Car.Detection.Research/car-classifier-research/src/hyp.verification.tools/py/test.png"
        if os.path.exists(filepath):
            image = cv2.imread(filepath)
        else:
            height = 250
            width = 250
            image = np.zeros((height,width,3), np.uint8)

        cv2.rectangle(image, (r1.getLeftXCoord(), r1.getTopYCoord()), (r1.getLeftXCoord()+r1.getWidth(), r1.getTopYCoord()+r1.getHeight()), (255, 255, 0), 1)
        # cv2.putText(image,"r1", (int(r1.getLeftXCoord() + 0.4 * r1.getWidth()), int(r1.getTopYCoord()+ 0.4*r1.getHeight())), cv2.FONT_HERSHEY_SIMPLEX, 0.25, 255)
        # cv2.putText(image,"r1"+str(r1), (int(r1.getLeftXCoord()), int(r1.getBottomYCoord())), cv2.FONT_HERSHEY_PLAIN, 0.5, 255)
        cv2.putText(image,"r1"+str(r1), (int(r1.getCenter().getXCoord()-0.5*r1.getWidth()), int(r1.getCenter().getYCoord())), cv2.FONT_HERSHEY_PLAIN, 0.5, 255)

        cv2.rectangle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), (r2.getLeftXCoord()+r2.getWidth(), r2.getTopYCoord()+r2.getHeight()), (0, 255, 0), 1)
        # cv2.putText(image,"r2", (int(r2.getLeftXCoord() + 0.4 * r2.getWidth()), int(r2.getTopYCoord()+ 0.4*r2.getHeight())), cv2.FONT_HERSHEY_SIMPLEX, 0.25, 255)
        cv2.putText(image,"r2"+str(r2), (int(r2.getCenter().getXCoord()-0.5*r2.getWidth()), int(r2.getCenter().getYCoord())), cv2.FONT_HERSHEY_PLAIN, 0.5, 255)

        cv2.circle(image,(r1.getCenter().getXCoord(), r1.getCenter().getYCoord()),2,(255, 255, 0), 1)
        cv2.circle(image,(r2.getCenter().getXCoord(), r2.getCenter().getYCoord()),2,(255, 255, 0), 1)


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
# print("---------------------------------")
# print("case: no intersection")
# print("---------------------------------")
# #correct
# r1 = Rectangle(0,5,5,5)
# r2 = Rectangle(0,100,5,5)
# test_instance.test(r1,r2)
#
#
# print("---------------------------------")
# print("case: fully contained rectangle")
# print("---------------------------------")
# #correct
# # r1 should contain r2, should be jaccard similar.
# r1 = Rectangle(0,0,50,50)
# r2 = Rectangle(0,0,40,40)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
# # r2 should contain r1
# r2 = Rectangle(0,0,50,50)
# r1 = Rectangle(0,0,40,40)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
#
# print("---------------------------------")
# print("case: x contained rectangle")
# print("---------------------------------")
# # correct
# r1 = Rectangle(0,100,50,50)
# r2 = Rectangle(20,100,20,100)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
#
#
# print("---------------------------------")
# print("case: y contained rectangle")
# print("---------------------------------")
# # correct
# r1 = Rectangle(10,0,100,100)
# r2 = Rectangle(0,5,50,30)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
#
# # correct
# r1 = Rectangle(10,0,50,100)
# r2 = Rectangle(0,5,20,30)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
#
#
# print("---------------------------------")
# print("case: not contained not parra intersect")
# print("---------------------------------")
# # correct
# r1 = Rectangle(0,0,50,50)
# r2 = Rectangle(25,25,50,50)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)

# r1 = Rectangle(16, 25, 89, 89)
# r2 = Rectangle(27, 38, 72, 52)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)


# print("---------------------------------")
# print("case:testing anomaly on images 26 No JI.")
# print("---------------------------------")
# r1 = Rectangle(16, 36, 82, 82)
# r2 = Rectangle(1, 31, 100, 64)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
#
# print("---------------------------------")
# print("case:testing anomaly on images 42 No JI.")
# print("---------------------------------")
# r1 = Rectangle(24, 32, 81, 81)
# r2 = Rectangle(6, 32, 95, 60)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)

# print("---------------------------------")
# print("case:testing anomaly on images 60 JI>1.")
# print("---------------------------------")
# r1 = Rectangle(38, 75, 22, 22)
# r2 = Rectangle(12, 29, 89, 66)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)
# # is for some reason doing union / intersection instead of int./ union

# print("---------------------------------")
# print("case:testing anomaly on images 60 JI>1.")
# print("---------------------------------")
# r1 = Rectangle(14, 21, 64, 64)
# r2 = Rectangle(4, 36, 95, 56)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)

# intersection: 2671
# union: 6745
# division result: 2
# jaccard index: 2.52527143392
# rectangles similar: True

# print("---------------------------------")
# print("case:JI seems to be correct")
# print("---------------------------------")
# r1 = Rectangle(0, 6, 117, 117)
# r2 = Rectangle(4, 36, 95, 56)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)

#fully contained.
# intersection: 13689
# union: 5320
# division result: 0
# jaccard index: 0.388633209146
# rectangles similar: True

# print("---------------------------------")
# print("case:testing anomaly on images 60 JI==None.")
# print("---------------------------------")
# r1 = Rectangle(19, 26, 82, 82)
# r2 = Rectangle(19, 31, 84, 59)
# test_instance.test(r1,r2)
# test_instance.printImage(r1,r2)


# print("---------------------------------")
# print("case:error. leftest.right is none")
# print("---------------------------------")
# r1 = Rectangle(51, 53, 71, 71)
# r2 = Rectangle(51, 28, 71, 81)
# test_instance.printImage(r1,r2)
# test_instance.test(r1,r2)


# print("---------------------------------")
# print("case:error. ")
# print("---------------------------------")
# r1 = Rectangle(133, 67, 24, 24)
# r2 = Rectangle(137, 32, 30, 19)
# test_instance.printImage(r1,r2)
# test_instance.test(r1,r2)


print("---------------------------------")
print("case:error. ")
print("---------------------------------")
r1 = Rectangle(114, 52, 57, 23)
r2 = Rectangle(75, 52, 84, 23)
test_instance.printImage(r1,r2)
test_instance.test(r1,r2)




# print(test_instance.simple_contains())
