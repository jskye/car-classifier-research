#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import cv2
from Rectangle import Rectangle
from scipy import misc
import numpy as np
import os.path
import math


# filepath = "/Users/juliusskye/COMP4120.Car.Detection.Research/car-classifier-research/src/hyp.verification.tools/py/test.png"
filepath = os.getcwd() + "/test.png"
if os.path.exists(filepath):
	image = cv2.imread(filepath)
else:
	height = 250
	width = 250
	image = np.zeros((height,width,3), np.uint8)

# r1 = Rectangle(0,0,100,100)
# r2 = Rectangle(0,100,20,20)
# r3 = Rectangle(0,200,20,20)
# cv2.rectangle(image, (r1.getLeftXCoord(), r1.getTopYCoord()), (r1.getLeftXCoord()+r1.getWidth(), r1.getTopYCoord()+r1.getHeight()), (0, 255, 0), 1)
# cv2.rectangle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), (r2.getLeftXCoord()+r2.getWidth(), r2.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
# cv2.rectangle(image, (r3.getLeftXCoord(), r3.getTopYCoord()), (r3.getLeftXCoord()+r3.getWidth(), r3.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
# cv2.circle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (40, r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (80, r2.getTopYCoord()), 5, (255, 0, 0), 1)


# test sliding vertical window
def testSlide(image):
	r1 = Rectangle(0,0,100,100)
	cv2.rectangle(image, (r1.getLeftXCoord()+50, r1.getTopYCoord()), (r1.getLeftXCoord()+r1.getWidth()+50, r1.getTopYCoord()+r1.getHeight()), (255, 0, 0), 1)
		# copy the detected rectangle
		# we use a deep copy because our Rectangle contain a Point.
		# r1_copy = copy.deepcopy(r1)
		# now we make N prop. windows

	numwindows = 5
	heightWidthRatioCar = 2.5

	# this can be potentially fixed up abit more. overlap wrt hypothesis.
	# but will do for now.
	for i in range(0,numwindows):
		print(i)
		# height of sliding window is height of avg car based on width of hypo. rectangle
		heightSlidingWindow = int(round(r1.getWidth() / heightWidthRatioCar))
		# print(heightSlidingWindow)
		# floorDiffSlidingWindow = heightSlidingWindow - math.floor(heightSlidingWindow)
		# ceilingDiffSlidingWindow = heightSlidingWindow - math.ceil(heightSlidingWindow)
		# if floorDiffSlidingWindow < ceilingDiffSlidingWindow:
		# 	heightSlidingWindow = int(math.floor(heightSlidingWindow))
		# elif ceilingDiffSlidingWindow < floorDiffSlidingWindow:
		# 	heightSlidingWindow = int(math.ceil(heightSlidingWindow))
		# else:
		# 	#choose ceiling for abit more height
		# 	heightSlidingWindow = int(math.ceil(heightSlidingWindow))

		print(heightSlidingWindow)
		# width is defaulted to same
		# TODO: in most cases width is smaller than car.
		# so could try bit more than width.
		widthSlidingWindow = r1.getWidth

		xSlidingWindow = r1.getLeftXCoord()
		# alternate printing color and stagger
		if i%2 == 0:
			color = (0, 255, 0)
			xSlidingWindow = r1.getLeftXCoord() - 50

		else:
			color = (0, 0, 255)

		ySlidingWindow = (r1.getTopYCoord()-heightSlidingWindow/2) + (r1.getHeight()/numwindows)*i
		slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, r1.getLeftXCoord()+r1.getWidth(), ySlidingWindow+heightSlidingWindow)
		print(slidingWindow)
		#print the sliding window

		cv2.rectangle(image, (slidingWindow.getLeftXCoord(), slidingWindow.getTopYCoord()), (slidingWindow.getLeftXCoord()+slidingWindow.getWidth(), slidingWindow.getHeight()), color, 1)
		# cv2.rectangle(image, (r1.getLeftXCoord(), r1.getTopYCoord()*i), (r1.getLeftXCoord()+r1.getWidth(), r1.getTopYCoord()*i+heightSlidingWindow), (0, 255, 0), 1)

testSlide(image)

misc.imsave(filepath, image)
# f.close()
