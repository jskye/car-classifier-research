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

# detected_rectangle = Rectangle(0,0,100,100)
# r2 = Rectangle(0,100,20,20)
# r3 = Rectangle(0,200,20,20)
# cv2.rectangle(image, (detected_rectangle.getLeftXCoord(), detected_rectangle.getTopYCoord()), (detected_rectangle.getLeftXCoord()+detected_rectangle.getWidth(), detected_rectangle.getTopYCoord()+detected_rectangle.getHeight()), (0, 255, 0), 1)
# cv2.rectangle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), (r2.getLeftXCoord()+r2.getWidth(), r2.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
# cv2.rectangle(image, (r3.getLeftXCoord(), r3.getTopYCoord()), (r3.getLeftXCoord()+r3.getWidth(), r3.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
# cv2.circle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (40, r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (80, r2.getTopYCoord()), 5, (255, 0, 0), 1)


# test sliding vertical window
def testSlide(image):
	detected_rectangle = Rectangle(50,50,150,150)
	print("detected_rectangle:" +str(detected_rectangle))
	cv2.rectangle(image, (detected_rectangle.getLeftXCoord(), detected_rectangle.getTopYCoord()), (detected_rectangle.getLeftXCoord()+detected_rectangle.getWidth(), detected_rectangle.getTopYCoord()+detected_rectangle.getHeight()), (255, 0, 0), -1)
		# copy the detected rectangle
		# we use a deep copy because our Rectangle contain a Point.
		# detected_rectangle_copy = copy.deepcopy(detected_rectangle)
		# now we make N prop. windows

	numwindows = 5
	heightWidthRatioCar = 2.5

	# this can be potentially fixed up abit more. overlap wrt hypothesis.
	# but will do for now.
	for i in range(0,5):
		print(i)
		# height of sliding window is height of avg car based on width of hypo. rectangle

		heightSlidingWindow = int(round(detected_rectangle.getWidth() / heightWidthRatioCar))
		widthSlidingWindow = detected_rectangle.getWidth()
		xSlidingWindow = detected_rectangle.getLeftXCoord()

		# alternate printing color and stagger
		if i ==(numwindows-1):
			color = (0, 255, 0)
			#stagger
			# xSlidingWindow = detected_rectangle.getLeftXCoord() - 50
		else:
			color = (0, 0, 255)

		if i ==(numwindows-1):
				ySlidingWindow = int(round((detected_rectangle.getTopYCoord()) + detected_rectangle.getWidth() / 3))
		else:
			ySlidingWindow = (detected_rectangle.getTopYCoord()) + (detected_rectangle.getHeight()/numwindows)*i
		slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow,heightSlidingWindow)
		print(slidingWindow)
		#print the sliding window
		cv2.rectangle(image, (slidingWindow.getLeftXCoord(), slidingWindow.getTopYCoord()), (slidingWindow.getLeftXCoord()+slidingWindow.getWidth(), slidingWindow.getTopYCoord()+slidingWindow.getHeight()), color, 1)


	# we also consider the car proportioned sliding window that bounds
	# the hypothesis vertically but not horizontally
	# so we scale width to potentially bound it horizontally too.
	# and update the hypothesis if that gets a better comparison.

	# height remains constant.
	heightSlidingWindow = detected_rectangle.getHeight()
	# width gets scaled according to car ratio.
	widthSlidingWindow = int(round(detected_rectangle.getWidth()*heightWidthRatioCar))
	# new x is current x - overhang
	overhang_percentage = (heightWidthRatioCar-1)/2
	overhang = detected_rectangle.getWidth()*overhang_percentage
	xSlidingWindow = int(round((detected_rectangle.getLeftXCoord() - overhang)))
	# new y is same
	ySlidingWindow = detected_rectangle.getTopYCoord()
	slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow, heightSlidingWindow)
	print(slidingWindow)
	# slidingWindows.append(slidingWindow)
	cv2.rectangle(image, (slidingWindow.getLeftXCoord(), slidingWindow.getTopYCoord()), (slidingWindow.getLeftXCoord()+slidingWindow.getWidth(), slidingWindow.getTopYCoord()+slidingWindow.getHeight()), color, 1)

testSlide(image)

misc.imsave(filepath, image)
# f.close()
