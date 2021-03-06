#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2015, Julius Sky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###############################################################################


'''
File: detect.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:
This program uses opencv's cascade function: detectMuliScale
to perfom detection with a given detector on a given image.

# The image can be preprocessed for diff color spaces:
# grayscale, YUV, HSV, HLS, CIELAB, CIELUV
# Note: by default, im.read outputs in BGR order not RGB
# For more info about convesion algorithms see:
# http://docs.opencv.org/master/de/d25/
# imgproc_color_conversions.html#color_convert_rgb_hls
# note: colorspace is deprecated. opencv doesnt implement this properly.
# it expects grayscale. grayscale is better for computation anyhow.
# it was badly documented initially.



For good default param values see:
http://www.searchalleasy.com/q/20801015/2589776
	Means checking scales 10percent of size increments
	scaleFactor=1.1
	Higher value results in less detections but with higher quality
	minNeighbors=5

	minSize=(30, 30)
	flags = cv2.cv.CV_HAAR_SCALE_IMAGE

	maxSize by default assumed size of image but can be set.

	use like this:

	# python cardetect.py image/path/image.extension cascade/path/cascade.xml colorspace
	# this is old. see args parsed below or see the batch shell script.

'''
from __future__ import division
from collections import OrderedDict
import os
import glob
import cv2
import sys
import time
import copy
import numpy as np
from scipy import misc
from CompareRectangles import CompareRectangles
from Rectangle import Rectangle
from Line import Line
from PIL import Image


# Get user supplied values
# TODO: use a more elegant param parser.
if len(sys.argv) == 8:
	cwd = sys.argv[0][:-3]
	imageDir = sys.argv[1]
	cascadePath = sys.argv[2]
	labelPath = sys.argv[3]
	imgresultspath = sys.argv[4]
	logresultspath = sys.argv[5]
	colorspace = sys.argv[6]
	min_neighbors = sys.argv[7]
	JI_THRESH = 0.35
elif len(sys.argv) == 9:
	cwd = sys.argv[0][:-3]
	imageDir = sys.argv[1]
	cascadePath = sys.argv[2]
	labelPath = sys.argv[3]
	imgresultspath = sys.argv[4]
	logresultspath = sys.argv[5]
	colorspace = sys.argv[6]
	min_neighbors = sys.argv[7]
	classifier_type = sys.argv[8]
	JI_THRESH = 0.35
elif len(sys.argv) == 10:
	cwd = sys.argv[0][:-3]
	imageDir = sys.argv[1]
	cascadePath = sys.argv[2]
	labelPath = sys.argv[3]
	imgresultspath = sys.argv[4]
	logresultspath = sys.argv[5]
	colorspace = sys.argv[6]
	min_neighbors = sys.argv[7]
	classifier_type = sys.argv[8]
	JI_THRESH = sys.argc[9]
else:
	print("check arguments!")

debugging = False
# for running live detection or testing how long detection takes.
livedetectionmode = False
# whether to use sliding windows when testing sides and comparing against groundtruths.
useslidingwindows = True

# keep a list of detection times.
detectiontime_list = []

# initiate variables
tot_True_positives = 0
tot_False_positives = 0
tot_False_neg = 0

# set noisy boolean based on image dir path.
# also set dataset based on image directory path
# either 4 chars till the 4th from the right or 4 till the 10th when noisy.
# "trai<ning>set/" or "trai<ning>set.noisy/"
# we couldve just passed a code in. but were already using alot of params.
noisytest = False
print(imageDir)
if imageDir[-6:] == "noisy/":
	print("noisy")
	noisytest = True
	dataset = imageDir[-14:-10]
else:
	dataset = imageDir[-8:-4]


if dataset == "ning" or dataset=="focu": #training or training.focused
	dataset = "training"
elif dataset == "test":
	dataset = "test"
elif dataset == "main": #publicdo<main>
	dataset = "pd"
# print(dataset)
# print(noisytest)
# exit()
testset = os.path.basename(imageDir[:-1])
# cwd = os.path.dirname(os.path.realpath(cascadePath))

# the results directory to put the final results (folders of images with detections labelled)
# testPath = "/Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/"
testPath = imgresultspath
labelName = os.path.basename(labelPath)
print("=================================================================")
print("============ RUNNING DETECTION ==================================")
print("=================================================================")
print("current working dir: "+testPath)
cascadePathWithoutExtension = cascadePath[:-4]
cascadeName = os.path.basename(cascadePath)
cascadeNameMinusEx = cascadeName[:-4]

print("using cascade: "+cascadeNameMinusEx+": "+cascadePathWithoutExtension)

# the directory to put the output logs
outputLogDir = logresultspath

# the output filename
outputFilename=testset+"."+cascadeNameMinusEx+'_'+colorspace+"MN"+min_neighbors+'_'+"TT"+classifier_type+'_'+'output.txt'
# save the output file here
outputDestination = outputLogDir+outputFilename

print("reading labelled rectangles from: "+labelPath)
print("printing results to: "+outputDestination)
# labelled_rectangles = {}
labelled_rectangles = OrderedDict()

# open and read the file with the labelled objects (eg. testset_rgb_100.txt)
# read each line as a list of rects

with open(labelPath, "r") as rects:
	#   for each rect in rects, read a rectangle as each set of four numbers
	#   excluding the first line number.
	#   TODO: check this code. looks hacky.
	for rect in rects:
	  labelled_rectangles[rect.split()[0]] = [rect.split()[1:][i:i+4]
	#   print(labelled_rectangles)
	  for i in range(0, len(rect.split()[1:]), 4)]
# print labelled_rectangles[0]

total_labelled_objects = len(labelled_rectangles)
print("total labelled objects: "+str(total_labelled_objects))


# load the trained cascade
print("loading classifier...")
# print(cascadePath)
trainedCascade = cv2.CascadeClassifier(cascadePath)

print("trained cascade is: "+str(trainedCascade))

# check if cascade is not empty.
if trainedCascade.empty():
	raise Exception("trained cascade is empty!")


total_objects_detected = 0

print("using JI_THRESH:"+str(JI_THRESH))


print("writing to output file: "+outputFilename)
with open(outputDestination, 'w') as results:
	results.write("*********************************\n")
	results.write("Batch Detection results \n")
	results.write("*********************************\n")
results.close()

print("loading images from: "+ str(imageDir))
# for imagePath in imageDir:
imageNum=0
images = sorted(glob.glob(imageDir+'*.jpg'))
for imagePath in images:
	img_True_positives=0
	img_False_positives=0
	img_False_neg =0
	imageName = os.path.basename(imagePath)
	print("--------------------------------------------------------")
	print("loading image for detection: "+imageName +", image number {0}".format(imageNum+1))
	if imageNum<len(images):
		imageNum =imageNum+1
	else: break

	# Read the image
	image = cv2.imread(imagePath)

	print("labelname: "+labelName)

	# convert to grayscale (default algorithm)
	# converting to other color spaces may be useless.
	# it seems colorspaces may not be implemented correctly in opencv.
	# this was not well documented in the docs.
	# see: http://stackoverflow.com/questions/30609018/opencv-detection-with-different-colorspace
	if colorspace == "gray":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	elif colorspace == "hsv":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	elif colorspace == "hls":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
	elif colorspace == "lab":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
	elif colorspace == "luv":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
	elif colorspace == "yuv":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
	elif colorspace =="rgb":
		colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	else:
		colorCVT = image

	print("using testset: " +testset)
	print('using color mode: '+colorspace)

	# print results to file
	with open(outputDestination, 'a') as results:
		results.write("Running detection on image:  "+imagePath +"\n")
		results.write("Detecting using trained classifier: "+cascadePath +"\n")
	results.close()


	# detection window PARAMS
	SCALE_FACTOR = 1.02
	MIN_NEIGHBORS = int(min_neighbors)
	MIN_SIZE = (10,10)
	MAX_SIZE = (128,128)

	print("using SCALE_FACTOR: " +str(SCALE_FACTOR))
	print("using MIN_NEIGHBORS: " + str(MIN_NEIGHBORS))
	print("using MIN_SIZE windows: " +str(MIN_SIZE))
	print("using MAX_SIZE windows: " +str(MAX_SIZE))

	# start timer
	# TODO: timertesting should be done without printing groundtruths, saving images.
	# since were just timing the detection.
	# in a real setting we would just detect and print to screen.
	detection_starttime = time.time()

	# Detect objects in the image
	detected_objects = trainedCascade.detectMultiScale(
		colorCVT,
		scaleFactor=SCALE_FACTOR,
		minNeighbors=MIN_NEIGHBORS,
		minSize=MIN_SIZE,
		maxSize=MAX_SIZE,
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)


	#TODO: finish
	# get rid of hypotheses that are contained inside others
	# because ... there shouldnt be a car within a car...
	detected_objects_clone = detected_objects
	# print(detected_objects_clone)


	# get rid of hypotheses that are contained inside others
	# because ... there shouldnt be a car within a car...
	# detected_objects_clone = copy.copy(detected_objects)
	iterations = int(len(detected_objects_clone))-1


	for this_index, this_detected_object in enumerate(detected_objects_clone[:-1]):
		# use the opencv returned rectangle and create our own.
		this_detected_rect = Rectangle(this_detected_object[0], this_detected_object[1], this_detected_object[2], this_detected_object[3])

		# print("this index (before second loop) is: {0}".format(this_index))

		# compare with those in front of this index.
		for that_index in range((this_index+1), len(detected_objects_clone)):
			# print(detected_objects_clone)
			# print("that index (before we get object) is: {0}".format(that_index))
			if that_index >= len(detected_objects_clone):
				break
			that_detected_object = detected_objects_clone[that_index]
			that_detected_rect = Rectangle(that_detected_object[0], that_detected_object[1], that_detected_object[2], that_detected_object[3])
			# get comparison of this and that rectangle.
			comparison_hypotheses = CompareRectangles(this_detected_rect, that_detected_rect, JI_THRESH)
			# print("this index is: {0}".format(this_index))
			# print("this rect is: {0}".format(this_detected_rect))
			# print("that index is: {0}".format(that_index))
			# print("that rect is: {0}".format(that_detected_rect))
			# if one of them is contained.
			if comparison_hypotheses.is_full_containment():
				# keep the container and remove the contained.
				contained = comparison_hypotheses.rect_fully_contained()
				# print("contained is: {0}".format(contained))
				# print("this detected rect is: {0}".format(this_detected_rect))
				# print("that detected rect is: {0}".format(that_detected_rect))
				# print(contained == this_detected_rect)
				# print(contained == that_detected_rect)

				# determine which is the contained.
				if contained == this_detected_rect:
					# detected_objects_clone.pop(this_index)
					detected_objects_clone = np.delete(detected_objects_clone, this_index, 0)
					if debugging:
						print("this rect is contained. removed this rectangle.")
				elif contained == that_detected_rect:
					# detected_objects_clone.delete(that_index)
					detected_objects_clone = np.delete(detected_objects_clone, that_index, 0)
					if debugging:
						print("that rect is contained. removed that rectangle")
				else:
					pass
					if debugging:
						print("hypothese not contained")

	# set resultant clone as the new list with contained hypotheses removed.
	detected_objects = detected_objects_clone
	# print(detected_objects_clone)




	if debugging:
		print("detected: " + str(len(detected_objects)) + " objects")

	# if we were in grayspace we want to convert back to rgb so we have colored
	# detection windows.
	if colorspace == 'gray':
		colorCVT = cv2.cvtColor(colorCVT, cv2.COLOR_GRAY2BGR)
	#     # rgbimg = Image.new("RGBA", (colorCVT.width, colorCVT.height))
	#     # rgbimg.paste(colorCVT)
	#     # colorCVT = rgbimg

	# initialise expected objects
	expectedObjects=0


	#draw the labelled rectangles
	# for testing detection time, this drawing is not done.
	# print('imageNum: '+imageNum)
	if not livedetectionmode:
		for labRect in labelled_rectangles[str(imageNum)]:
			expectedObjects+=1
			# print(expectedObjects)

			# if focused:
			if classifier_type == "S" and dataset =="training":
				x = int(labRect[0]) + int((110-100)/2)
				y = int(labRect[1]) + int((110-40)/2)
			else:
				x = int(labRect[0])
				y = int(labRect[1])
			w = int(labRect[2])
			h = int(labRect[3])
			# print("printing rectangle: {0}.{1}: ({2},{3},{4},{5})".format(imageNum,expectedObjects,x,y,w,h))

			# if colorspace =='lab' or 'luv':
			#     groundColor = (0, 0, 255)
			# else:
			groundColor = (0, 0, 255)

			cv2.rectangle(colorCVT, (x, y), (x+w, y+h), groundColor, 1)


	# Draw detected objects
	for (detx, dety, detectedWidth, detectedHeight) in detected_objects:

		# use the opencv returned rectangle and create our own.
		detected_rectangle = Rectangle(detx, dety, detectedHeight, detectedWidth)


		# we use sliding windows of similar proportions to car sides
		# within the feature hypothesis, to compare the hypothesis
		# with the groundtruths when testing side car classifiers.
		# If the comparison is better than with the original hypothesis,
		# then we use that result.
		# We do this because when we compare to JI, it wont be similar
		# because ground truths are cropped to the car and the collated features
		# return us square (assumed to bound the features).
		# TODO: this assumption should be checked, how the minneighbors
		# collates features in opencv.
		# By considering rectangles
		# sometimes the first check will be better and quite good,
		# and we will waste computation and time by checking others.
		# so, sliding window should be accepted if JI under certain limit.
		#

		#
		# so what we can do is keep the width of the hypothesis the same.
		# but contract the height so that its in more similar proportions to a side car.
		# but if we just kept the middle of the hypothesis, sometimes this might
		# not be ideal (eg. the car might be in the bottom part of hypothesis)
		# so we check top/middle/bottom (or N proportioned sliding windows) etc.
		# for the most similar (proportioned) window to the labelled car.
		# TODO: actually this is a valid strategy for livedetectionmode if
		# we just wish to guess the middle portion of the square hypothesis.
		# because most of the time, the car is in the middle.

		# if classifier_type == "S" and not livedetectionmode and useslidingwindows:
		if classifier_type == "S" and useslidingwindows:
			# see if any proportioned sliding windows are better than hypothesis

			# numwindows = 5

			# 1.5-2.5 seems to give very similar results.
			heightWidthRatioCar = 2.5
			slidingWindows = []


			# keeping width constant, define new height of hypothesis window
			heightSlidingWindow = int(round(detected_rectangle.getWidth() / heightWidthRatioCar))
			# width defaults to same
			widthSlidingWindow = detected_rectangle.getWidth()
			xSlidingWindow = detected_rectangle.getLeftXCoord()
			# sliding window is in middle of hypothesis.
			ySlidingWindow = int(round((detected_rectangle.getTopYCoord()) + detected_rectangle.getWidth() / 3))
			slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow,heightSlidingWindow)
			slidingWindows.append(slidingWindow)
			# print(slidingWindow)


			# deprecated: its not really valid to use the best slidingwindow
			# in testing but only have the ability to choose a middle one live.
			# for i in range(0,numwindows-1):
			# 	# print(i)
			#
			# 	# we first consider when hypothesis bounds width of car.
			# 	# but height is too big to get valid comparison.
			# 	# in this case, height is a portion of the hypothesis height.
			#
			# 	# keeping width constant, define new height of hypothesis window
			# 	heightSlidingWindow = int(round(detected_rectangle.getWidth() / heightWidthRatioCar))
			# 	# width defaults to same
			# 	widthSlidingWindow = detected_rectangle.getWidth()
			# 	xSlidingWindow = detected_rectangle.getLeftXCoord()
			#
			# 	# print windows when debugging.
			# 	if debugging:
			# 		# alternate printing color and stagger
			# 		if i ==(numwindows-1):
			# 			color = (0, 255, 0)
			# 			#stagger
			# 			# xSlidingWindow = detected_rectangle.getLeftXCoord() - 50
			# 		else:
			# 			color = (0, 0, 255)
			#
			# 	if i ==0:
			# 			# sliding window is in middle of hypothesis.
			# 			ySlidingWindow = int(round((detected_rectangle.getTopYCoord()) + detected_rectangle.getWidth() / 3))
			# 			slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow,heightSlidingWindow)
			# 			slidingWindows.append(slidingWindow)
			# 	ySlidingWindow = int(round((detected_rectangle.getTopYCoord()) + (detected_rectangle.getHeight()/numwindows)*i))
			# 	slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow,heightSlidingWindow)
			# 	slidingWindows.append(slidingWindow)
				# print(slidingWindow)
				#print the sliding window
				# cv2.rectangle(image, (slidingWindow.getLeftXCoord(), slidingWindow.getTopYCoord()), (slidingWindow.getLeftXCoord()+slidingWindow.getWidth(), slidingWindow.getTopYCoord()+slidingWindow.getHeight()), color, 1)


			# # the validity of having another guess based on proportion depends on use case.
			# # extending width deprecated:
 		# 	# could make new Hypo inaccurate if initial Hyp was bounding the width tightly.
			#
			# # the car proportioned sliding window that bounds
			# # the hypothesis vertically but not horizontally
			# # so we scale width to potentially bound it horizontally too.
			# # and update the hypothesis if that gets a better comparison.
			#
			# # height remains constant.
			# heightSlidingWindow = detected_rectangle.getHeight()
			# # width gets scaled according to car ratio.
			# widthSlidingWindow = int(round(detected_rectangle.getWidth()*heightWidthRatioCar))
			# # new x is current x - overhang
			# overhang_percentage = (heightWidthRatioCar-1)/2
			# overhang = detected_rectangle.getWidth()*overhang_percentage
			# xSlidingWindow = int(round((detected_rectangle.getLeftXCoord() - overhang)))
			# # new y is same
			# ySlidingWindow = detected_rectangle.getTopYCoord()
			# slidingWindow = Rectangle(xSlidingWindow, ySlidingWindow, widthSlidingWindow, heightSlidingWindow)
			# # print(slidingWindow)
			# slidingWindows.append(slidingWindow)
			# # cv2.rectangle(image, (slidingWindow.getLeftXCoord(), slidingWindow.getTopYCoord()), (slidingWindow.getLeftXCoord()+slidingWindow.getWidth(), slidingWindow.getTopYCoord()+slidingWindow.getHeight()), color, 1)


		if debugging:
			print('the detected rectangle: '+ str(detected_rectangle))
		detectedArea = detected_rectangle.area()


		# get the labelled rectangle to compare the detection with.
		# Note. the below is relevant to testing against known labelled groundtruths.
		# in a live system, your not evaluating against groundtruths.
		# the feature (collated feature group) forms an unverifiable hypothesis.
		# if the classifier is trained well, then it should evaluate well
		# when comparing to groundtruths in testing and to the eye when live.

		# we will compare the detection with that labelled rectangle
		# that is closest and most similar in area.
		# we dont want to compare to all labelled rectangles,
		# because detection might be only just dissimilar to a labelled
		# rectangle because it picked up certain features but not enough,
		# but is completely dissimilar to other labelled rectangles elsewhere.

		# two rects will be considered as in same neighborhood if
		# difference between distance(r1, r2) and distance(r1,r3)
		# is under some constant
		PROXIMAL_RECTS_CONSTANT = 2

		if debugging:
			print("finding rectangle to compare detected to from the labelled rectangles: "+ str(labelled_rectangles[str(imageNum)]))
		# print("print of labelled dictionary: " + str(labelled_rectangles))

		# loop through each image's labelled rectangles
		# decide which labelled rectangle is most appropriate to compare detection to.
		# note: the sliding windows will be somewhere more or less inside or about the detected.
		# so we can just keep this calculated for the detected before seeing if slidingwindows are more similar.

		# initialise loop
		iteration = 0
		labelled_rectangle = None
		closest_rectangle = None

		# each image may have 1 or many labelled rectangles.
		for labelled_rect in labelled_rectangles[str(imageNum)]:
			# labelled_rectangle = labelled_rects[iteration]
			# print('image: ' + str(imageNum) + ', - labelled rect: '+str(labelled_rect))

			# only one label in this image
			if len(labelled_rectangles[str(imageNum)]) ==1:
					if classifier_type == "S" and dataset =="training":
						relabel_x = int(labRect[0]) + int((110-100)/2)
						relabel_y = int(labRect[1]) + int((110-40)/2)
						labelled_rectangle_to_compare = Rectangle(relabel_x,relabel_y, int(labelled_rect[2]), int(labelled_rect[3]))
					else:
						labelled_rectangle_to_compare = Rectangle(int(labelled_rect[0]),int(labelled_rect[1]), int(labelled_rect[2]), int(labelled_rect[3]))
			#many labels
			else:

				if iteration == 0:
					if classifier_type == "S" and dataset =="training":
						relabel_x = int(labRect[0]) + int((110-100)/2)
						relabel_y = int(labRect[1]) + int((110-40)/2)
						closest_labelled_rectangle = Rectangle(relabel_x,relabel_y, int(labelled_rect[2]), int(labelled_rect[3]))
					else:
						closest_labelled_rectangle = Rectangle(int(labelled_rect[0]),int(labelled_rect[1]), int(labelled_rect[2]), int(labelled_rect[3]))

					# define first labelled rectangle as closest
					current_path = Line(detected_rectangle.getCenter(), closest_labelled_rectangle.getCenter())
					closest_distance = current_path.getDistance()
					labelled_rectangle_to_compare = closest_labelled_rectangle

				else:

					if classifier_type == "S" and dataset =="training":
						relabel_x = int(labRect[0]) + int((110-100)/2)
						relabel_y = int(labRect[1]) + int((110-40)/2)
						labelled_rectangle = Rectangle(relabel_x,relabel_y, int(labelled_rect[2]), int(labelled_rect[3]))
					else:
						labelled_rectangle = Rectangle(int(labelled_rect[0]),int(labelled_rect[1]), int(labelled_rect[2]), int(labelled_rect[3]))

					# get straight line distance between the center of labelled and detection rectangles.
					current_path = Line(detected_rectangle.getCenter(), labelled_rectangle.getCenter())
					current_distance = current_path.getDistance()

					# if the difference between the detected rectangle and the two labelled rectangles is small, then theyre in same neighborhood.
					in_same_neighborhood = (current_distance-closest_distance) < PROXIMAL_RECTS_CONSTANT
					# print("dist between" + str(labelled_rectangle) +"and" +str(detected_rectangle) + "is: "+str(current_distance))

					# update the rectangle that should be compared if this rectangle is closer to previous,
					# where the two detections are not in same neighborhood.
					if  (current_distance < closest_distance) and not in_same_neighborhood:
						# print('current dist < closet dist and NOT IN same neighborhood')
						closest_distance = current_distance
						current_path = Line(detected_rectangle.getCenter(), labelled_rectangle_to_compare.getCenter())
						closest_labelled_rectangle = labelled_rectangle
						labelled_rectangle_to_compare = closest_labelled_rectangle

					# where the new distanc is closer but the two detections are in same neighborhood.
					# only update if new label has greater JI
					elif (current_distance < closest_distance) and in_same_neighborhood:
						# print('current dist < closest dist and IN same neighborhood')
						if debugging:
							print('detected rectangle: ' + str(detected_rectangle) + '\n labelled rectangle to compare: '+ str(labelled_rectangle_to_compare))
						comparison_detection_and_labelled_to_compare = CompareRectangles(detected_rectangle, labelled_rectangle_to_compare, JI_THRESH)
						jacc_index_detection_and_labelled_to_compare = comparison_detection_and_labelled_to_compare.jaccard_index()
						comparison_detection_and_labelled = CompareRectangles(detected_rectangle, labelled_rectangle, JI_THRESH)
						jacc_index_detection_and_labelled = comparison_detection_and_labelled.jaccard_index()
						# comparison to this label is more appropriate than to current labelled_rectangle_to_compare
						if max(jacc_index_detection_and_labelled_to_compare, jacc_index_detection_and_labelled) == jacc_index_detection_and_labelled:
							if debugging:
								print('new labelled rectangle is more relevant to compare')
							labelled_rectangle_to_compare = labelled_rectangle
						else:
							if debugging:
								print('new labelled rectangle is NOT more relevant to compare')
							labelled_rectangle_to_compare = labelled_rectangle_to_compare
					else:
						pass
						# print('currnt dist > closest dist')

				iteration+=1
			if debugging:
				print("most appropriate rectangle to compare detected to is: "+ str(labelled_rectangle_to_compare))



		# draw detected rectangle only if rectangles are similar according to Jaccard Index.
		# compare detected object with closest labelled rectangle
		# if true positive found, then stop comparing.


		if debugging:
			print('detected rectangle to compare'+str(detected_rectangle))
			print('labelled rectangle to comapre'+str(labelled_rectangle_to_compare))



		# compare the detection with the labelled_rectangle_to_compare
		rectangle_comparison = CompareRectangles(detected_rectangle,labelled_rectangle_to_compare, JI_THRESH)
		# get the jaccard index (used later on)
		det_jaccard_index = rectangle_comparison.jaccard_index()
		# get jaccard index of comparisons with the sliding windows.
		if classifier_type == "S" and useslidingwindows:
			break_limit = 0.7
			for slidingWindow in slidingWindows:
				sw_comparison = CompareRectangles(slidingWindow,labelled_rectangle_to_compare, JI_THRESH)
				if debugging:
					print("slidingwindow: {0} vs labelrect: {1}, JITHRESH:{2}".format(slidingWindow, labelled_rectangle_to_compare, JI_THRESH))
				sw_jaccard_index = sw_comparison.jaccard_index()
				if debugging:
					print("hypothesis_JI: {0}, slidingwindow_JI: {1}".format(det_jaccard_index, sw_jaccard_index))
				if sw_jaccard_index > break_limit and sw_jaccard_index > det_jaccard_index:
					# update hypothesis
					detected_rectangle = slidingWindow
					det_jaccard_index = sw_jaccard_index
					# update rectangle comparison
					rectangle_comparison = CompareRectangles(detected_rectangle,labelled_rectangle_to_compare, JI_THRESH)
					# break loop cos we dont wanna waste computation/time
					if debugging:
						print("this sliding window is significantly better, confident is car, stop looking")
					break
				# if not awesome similar but still better
				elif sw_jaccard_index < break_limit and sw_jaccard_index > det_jaccard_index:
						# update but dont break, so check others.
						# update hypothesis
						detected_rectangle = slidingWindow
						det_jaccard_index = sw_jaccard_index
						# update rectangle comparison
						rectangle_comparison = CompareRectangles(detected_rectangle,labelled_rectangle_to_compare, JI_THRESH)
						if debugging:
							print("this sliding window is somewhat better, keep looking")
				else: # JI not better, we continue looking for better hypothesis in slidingwindows
					if debugging:
						print("JI not better")
					continue



		# determine if rectangles similar, using the Jaccard threshold if its set.
		jaccard_similar = rectangle_comparison.similar_rectangles()

		if debugging:
			print('Jaccard Index: '+str(det_jaccard_index))

		# print false positives in red
		if not jaccard_similar:
			if debugging:
				print('rectangles ARE NOT jaccard similar')
			cv2.rectangle(colorCVT, (detx, dety), (detx+detectedWidth, dety+detectedHeight), (255, 0, 0), 1)
			img_False_positives +=1
		# detected_rectangle is true positive if jaccard similar (JI > 0.5)
		else:
			if debugging:
				print('rectangles ARE jaccard similar')
			# print true positive in blue
			cv2.rectangle(colorCVT,
			(detected_rectangle.getLeftXCoord(),
			 detected_rectangle.getTopYCoord()),
			 (detected_rectangle.getLeftXCoord()+detected_rectangle.getWidth(),
			  detected_rectangle.getTopYCoord()+detected_rectangle.getHeight()),
			   (0, 255, 0), 2)
			# cv2.rectangle(colorCVT, (0,0), (1,1), (0,0,255),2)
			img_True_positives +=1
			# break


		detection_endtime = time.time()
		detectiontime = detection_endtime-detection_starttime
		if debugging:
			print("detection and printing hypthesese to screen took: "+str(detectiontime))
		detectiontime_list.append(detectiontime)

	# increment False negatives
	if expectedObjects>0 and len(detected_objects)<1:
		img_False_neg = expectedObjects - img_True_positives
		tot_False_neg+=img_False_neg

	tot_True_positives +=img_True_positives
	tot_False_positives += img_False_positives

	# print("TP:{0}, FP: {1}, FN: {2}".format(img_True_positives, img_False_positives, img_False_neg), colorCVT)


	# append to end of file
	with open(outputDestination, 'a') as results:
		results.write("TP:{0}, FP: {1}, FN: {2}".format(img_True_positives, img_False_positives, img_False_neg))
		results.write("\n")
		results.write("\n")
	results.close()




	# create directory to save results
	resultsDir = testPath+"results."+testset+"."+cascadeNameMinusEx+"."+colorspace+"MN"+min_neighbors
	if not os.path.isdir(resultsDir):
		os.makedirs(resultsDir)

	# save image with detections drawn on
	outputDir = cascadePathWithoutExtension
	# misc.imsave(cwd+'/'+outputDir+'/detected_'+imagePath, colorCVT)
	misc.imsave(resultsDir+'/detected_'+imageName, colorCVT)

	#increment total detected objects
	total_objects_detected = total_objects_detected+len(detected_objects)




# print("Total objects detected: {0}".format(len(objects)))
with open(outputDestination, 'a') as results:
	results.write("Total labelled objects: {0}".format(total_labelled_objects))
	results.write("\n")
	results.write("Total objects detected: {0}".format(total_objects_detected))
	results.write("\n")
	results.write("Total TP:{0}, Total FP: {1}, Total FN: {2}".format(tot_True_positives, tot_False_positives, tot_False_neg))
	results.write("\n")

	if total_labelled_objects != 0:
		# True positive rate (sensitivity/hitrate/recall)
		tpr = tot_True_positives/total_labelled_objects
		# fall-out or False positive rate (FPR)
		fpr = tot_False_positives/total_labelled_objects
	else:
		tpr = 0
		fpr = 0

	# results.write("Total TPR:{0}, Total FPR: {1}".format(tpr, fpr))
	# results.write("\n")

	# Positive Likelyhood ratio: LR+ = TPR/FPR.
	if fpr != 0:
		LRPlus = tpr/fpr
	else:
		LRPlus = None

	#Precision or positive predictive value (PPV) ­ Calculated using PPV = TP/(TP+FP).
	if (tot_True_positives + tot_False_positives) != 0:
		PPV = tot_True_positives/(tot_True_positives + tot_False_positives)
	else:
		PPV = None

	# precision is the number of correct positive results divided by the number of all positive results
	# recall is the number of correct positive results divided by the number of positive results that should have been returned.

	delta = 0.0001

	precision = tot_True_positives/(tot_True_positives+tot_False_positives+delta)
	recall = tot_True_positives/ (tot_True_positives + tot_False_neg+delta)
	#harmonic mean = 2 ((precisin x recall)/(precision + recall))
	harmonic_mean = ((precision*recall) / (precision+recall+delta))*2

	# average detection time
	if len(detectiontime_list) != 0:
		adt = np.mean(detectiontime_list)
	else:
		 adt = 0.0

	results.write("ADT: {0:.2f} seconds \n".format(adt))
	results.write("TPR: {0} \n".format(tpr))
	results.write("FPR: {0} \n".format(fpr))
	results.write("PPV: {0} \n".format(PPV))
	results.write("LR+: {0} \n".format(LRPlus))
	results.write("Precision: {0} \n".format(precision))
	results.write("Recall: {0} \n".format(recall))
	results.write("Harmonic Mean: {0} \n".format(harmonic_mean))

	results.write("\n")
results.close()

print("Total labelled objects: {0}".format(total_labelled_objects))
print("\n")
print("Total objects detected: {0}".format(total_objects_detected))
print("\n")
print("Total TP:{0}, Total FP: {1}, Total FN: {2}".format(tot_True_positives, tot_False_positives, tot_False_neg))
print("\n")
# print("Detection Times: {0} \n".format(str(detectiontime_list)))
print("Average Time to detect hypotheses per image: {0:.2f} seconds \n".format(adt))
print("TPR: {0} \n".format(tpr))
print("FPR: {0} \n".format(fpr))
print("PPV: {0} \n".format(PPV))
print("LR+: {0} \n".format(LRPlus))
print("Precision: {0} \n".format(precision))
print("Recall: {0} \n".format(recall))
print("Harmonic Mean: {0} \n".format(harmonic_mean))

if noisytest:
	varyoutputfile = outputLogDir+"varyneighbors/{0}.{1}.noisy.txt".format(cascadeNameMinusEx, dataset)
else:
	varyoutputfile = outputLogDir+"varyneighbors/{0}.{1}.txt".format(cascadeNameMinusEx, dataset)

with open(varyoutputfile, 'a') as results:
	results.write("{0}\t".format(min_neighbors))
	results.write("{0:.2f}\t".format(precision))
	results.write("{0:.2f}\t".format(recall))
	results.write("{0:.2f}\t".format(harmonic_mean))
	results.write("{0:.2f}\n".format(adt))
print("finished detection and evaluation")
print("=================================================================")
	# cv2.imshow("Found {0} objects!".format(len(objects)), colorCVT)
	# cv2.waitKey(0)
